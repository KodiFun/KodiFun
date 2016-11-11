import xbmcaddon
import xbmcgui
import xbmcplugin
import os
import sys
import locale

__plugin__ = 'script.diceroller.game'
__author__ = 'KodiFun'
__url__ = 'https://github.com/KodiFun/KodiFun'
__date__ = '11-11-2016'
__version__ = '0.0.01'
__theme__ = 'Default'

__addon__     = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__settings__  = xbmcaddon.Addon(__plugin__)
__language__  = __settings__.getLocalizedString
__apath__ = xbmc.translatePath(__addon__.getAddonInfo('path'))
__themepath__ = os.path.join(__apath__,'resources','skins',__theme__,'720p')

xbmc.log(__addonname__)
xbmcgui.Dialog().ok(__addonname__, "hello", "world", "My first addon") 