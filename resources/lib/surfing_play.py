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
import urlparse
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

class Main:
    def __init__(self):
        # Get plugin settings
        self.DEBUG = __settings__.getSetting('debug')
                
        if (self.DEBUG) == 'true':
            xbmc.log( "[ADDON] %s v%s (%s) debug mode, %s = %s, %s = %s" % ( __addon__, __version__, __date__, "ARGV", repr(sys.argv), "File", str(__file__) ), xbmc.LOGNOTICE )
                
        # Parse parameters
        params = urlparse.parse_qs(urlparse.urlparse(sys.argv[2]).query)
        url = params['url'][0]
        
        # Load heat detail
        api = SurfingAPI()
        heat = api.get(url)
        self.play_url = heat['stream_url']
        self.title = heat['title']
        
        #
        # Play video
        #
        self.playVideo()
        
    #
    # Play video
    #
    def playVideo(self):
        try:
            listitem = xbmcgui.ListItem(label=self.title, iconImage="DefaultVideo.png", thumbnailImage="DefaultVideo.png")
            listitem.setInfo('video', { "title": self.title, "studio" : "ASP", "genre" : "Sports" })
            #if hasattr(listitem, 'addStreamInfo'):
            #        listitem.addStreamInfo('audio', p.get_xbmc_audio_stream_info())
            #        listitem.addStreamInfo('video', p.get_xbmc_video_stream_info())
            xbmc.Player().play(self.play_url, listitem)
        except:
            # oops print error message
            d = xbmcgui.Dialog()
            message = self.dialog_error("Unable to play video")
            d.ok(*message)

    def dialog_error(self, msg):
        # Generate a list of lines for use in XBMC dialog
        content = []
        exc_type, exc_value, exc_traceback = sys.exc_info()
        content.append("%s v%s Error" % (__addon__, __version__))
        content.append("%s (%d) - %s" % (exc_traceback.tb_frame.f_code.co_name, exc_traceback.tb_lineno, msg))
        content.append(str(exc_value))
        return content
        