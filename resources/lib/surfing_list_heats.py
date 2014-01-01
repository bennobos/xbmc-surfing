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

from surfing_const import __addon__, __settings__, __language__, __images_path__, __date__, __version__
from surfing_api import SurfingAPI

import os
import re
import sys
import urllib
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

class Main:
    def __init__(self):
        # Get plugin settings
        self.DEBUG = __settings__.getSetting('debug')
        
        if (self.DEBUG) == 'true':
            xbmc.log("[ADDON] %s v%s (%s) debug mode, %s = %s, %s = %s" % (__addon__, __version__, __date__, "ARGV", repr(sys.argv), "File", str(__file__)), xbmc.LOGNOTICE)
        
        # Parse parameters
        params = urlparse.parse_qs(urlparse.urlparse(sys.argv[2]).query)
        url = params['url'][0]
        
        # Retrieve the round detail, including heats.
        api = SurfingAPI()
        round = api.get(url)
        for h in round['heats']:
            detail_url = '/heats/' + str(h['id'])
            parameters = {"action" : "play", "plugin_category" : h['title'], "url" : detail_url, "next_page_possible": "True"}
            url = sys.argv[0] + '?' + urllib.urlencode(parameters)
            listitem = xbmcgui.ListItem(h['title'], iconImage="DefaultFolder.png")
            xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url=url, listitem=listitem, isFolder=True)

        # Disable sorting
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )

        # End of list
        xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
        