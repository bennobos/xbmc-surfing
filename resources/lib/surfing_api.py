# Copyright (C) 2014 CodeFish
#
# This file is part of XBMC-aspsurfing.
#
# XBMC-aspsurfing is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# XBMC-aspsurfing is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with XBMC-aspsurfing.  If not, see <http://www.gnu.org/licenses/>.
  
from surfing_const import __settings__

import json
import urllib2
import xbmc

class SurfingAPI:
    def __init__(self):
        # Get plugin settings
        self.DEBUG = __settings__.getSetting('debug')
        self.API_URL = __settings__.getSetting('api_url')
        
    # Retrieve data by calling the API.
    # The result is json.
    def get(self, path):
        url = self.API_URL + path
        if (self.DEBUG) == 'true':
            xbmc.log("[ADDON] Using url: %s" % (url), xbmc.LOGNOTICE)
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20100101 Firefox/22.0')
        response = urllib2.urlopen(req)
        data = response.read()
        response.close()
        return json.loads(data)
