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

__addon__       = "plugin.video.aspsurfing"
__version__     = "1.0.0"

#
# Imports
#
import os
import re
import sys
import urlparse
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

LIB_DIR = xbmc.translatePath(os.path.join(xbmcaddon.Addon(id=__addon__).getAddonInfo('path'), 'resources', 'lib'))
sys.path.append(LIB_DIR)

# Get plugin settings
DEBUG = xbmcaddon.Addon(id=__addon__).getSetting('debug')

# Parse parameters
if len(sys.argv[2]) == 0:
    #
    # Main menu
    #
    if (DEBUG) == 'true':
        xbmc.log("[ADDON] %s v%s is starting, ARGV=%s" % (__addon__, __version__, repr(sys.argv)), xbmc.LOGNOTICE)
    import surfing_main as plugin
else:
    action = urlparse.parse_qs(urlparse.urlparse(sys.argv[2]).query)['action'][0]
    if (DEBUG) == 'true':
        xbmc.log("[ADDON] action=%s, ARGV=%s" % (action, repr(sys.argv)), xbmc.LOGNOTICE)
    #
    # List rounds
    #
    if action == 'list_rounds':
        import surfing_list_rounds as plugin
    #
    # List heats
    #
    if action == 'list_heats':
        import surfing_list_heats as plugin
    #
    # Play
    #
    elif action == 'play':
        import surfing_play as plugin

# Delegate to plugin
plugin.Main()