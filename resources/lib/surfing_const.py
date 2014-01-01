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

import os
import xbmcaddon

__addon__       = "plugin.video.aspsurfing"
__settings__    = xbmcaddon.Addon(id=__addon__ )
__language__    = __settings__.getLocalizedString
__images_path__ = os.path.join( xbmcaddon.Addon(id=__addon__ ).getAddonInfo('path'), 'resources', 'images' )
__date__        = "1 january 2014"
__version__     = "1.0.0"
