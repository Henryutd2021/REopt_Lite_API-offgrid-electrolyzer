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


url = 'https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-download.csv?wkt=POINT(-96.78%2032.77)&names=2019&leap_day=' \
      'false&interval=60&utc=false&full_name=henry_li&email=hxl210015@utdallas.edu&affiliation=ut-dallas&mailing_list=' \
      'false&reason=beta_testing&api_key=86DIek0E1Nt1h5CZNNBY9KHC9ISpv7PNOLGbA90o&attributes=dhi,dni,ghi,dew_point,air_temperature,' \
      'surface_pressure,relative_humidity,wind_direction,wind_speed,surface_albedo'

ur.urlretrieve(url, 'data.csv')
def CSPCF():
    csp_model = pycsp.default('MSPTSingleOwner')
    csp_model.SolarResource.solar_resource_file = 'data.csv'
    csp_model.execute()
    prod_factor_original = [power * 1000 / csp_model.Outputs.system_capacity for power in csp_model.Outputs.P_out_net]
    return prod_factor_original

