# *********************************************************************************
# REopt, Copyright (c) 2019-2020, Alliance for Sustainable Energy, LLC.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list
# of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright notice, this
# list of conditions and the following disclaimer in the documentation and/or other
# materials provided with the distribution.
#
# Neither the name of the copyright holder nor the names of its contributors may be
# used to endorse or promote products derived from this software without specific
# prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
# *********************************************************************************

import PySAM.TcsmoltenSalt as pycsp  # import the TcsmoltenSalt from PySAM
import urllib.request as ur
from keys import developer_nrel_gov_key
from .wind import time_step_hour_to_minute_interval_lookup
import logging
log = logging.getLogger(__name__)
import numpy as np

class CSPSAM():

    def __init__(self,
                 url_base="https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-download.csv",
                 latitude=None,
                 longitude=None,
                 year=2019,
                 api_key=developer_nrel_gov_key,
                 attributes='dhi,dni,ghi,dew_point,air_temperature,surface_pressure,relative_humidity,wind_direction,'
                            'wind_speed,surface_albedo',
                 your_name='henry_li',
                 utc='false',
                 your_affiliation='ut-dallas',
                 reason_for_use='beta_testing',
                 your_email='hxl210015@utdallas.edu',
                 mailing_list='false',
                 time_steps_per_hour=1,
                 leap_year='false',
                 **kwargs
                 ):
        self.url_base = url_base
        self.leap_year = leap_year
        self.mailing_list = mailing_list
        self.reason_for_use = reason_for_use
        self.your_email = your_email
        self.your_affiliation = your_affiliation
        self.utc = utc
        self.attributes = attributes
        self.latitude = latitude
        self.longitude = longitude
        self.key = api_key
        self.your_name = your_name
        self.year = year
        self.time_steps_per_hour = time_steps_per_hour
        self.interval = time_step_hour_to_minute_interval_lookup[round(float(time_steps_per_hour), 2)]
        #self.interval = '60'

    @property
    def url(self):
        url = self.url_base+'?wkt=POINT({lon}%20{lat})&names={year}' \
              '&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}' \
              '&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=self.year,
            lat=self.latitude, lon=self.longitude, leap=self.leap_year, interval=self.interval,
            utc=self.utc, name=self.your_name, email=self.your_email, mailing_list=self.mailing_list,
            affiliation=self.your_affiliation, reason=self.reason_for_use, api=self.key, attr=self.attributes)
        return url


    def CSPPF(self):
        ur.urlretrieve(self.url, 'data.csv')
        log.info("NSRDB query for CSP successful.")
        csp_model = pycsp.default('MSPTSingleOwner')
        csp_model.SolarResource.solar_resource_file = 'data.csv'
        csp_model.execute()
        prod_factor_original = [power * 1000 / csp_model.Outputs.system_capacity for power in
                                csp_model.Outputs.P_out_net]
        for i, x in enumerate(prod_factor_original):
            if x >= 1:
                prod_factor_original[i] = 1.0
            elif x <= 0:
                prod_factor_original[i] = 0.0
        return prod_factor_original


