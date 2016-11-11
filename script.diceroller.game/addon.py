import xbmcaddon
import xbmcgui
import xbmcplugin
# import re, time, urllib2, urlparse
import os
import sys
import locale
# import test
import dialog

__plugin__ = 'script.diceroller.game'
__author__ = 'KodiFun'
__url__ = 'https://github.com/KodiFun/KodiFun'
__date__ = '28-08-2016'
__version__ = '0.0.03'
__theme__ = 'Default'

__addon__     = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__settings__  = xbmcaddon.Addon(__plugin__)
__language__  = __settings__.getLocalizedString
__apath__ = xbmc.translatePath(__addon__.getAddonInfo('path'))
__themepath__ = os.path.join(__apath__,'resources','skins',__theme__,'720p')

parental_code     = __settings__.getSetting("32000")
parental_control  = __settings__.getSetting("32001")
__bLogging__  =__settings__.getSetting("32004")
xbmc.log("Debugging = " + str(__bLogging__))
sys.path.insert(0, os.path.join(__apath__, 'resources', 'src'))

xbmc.log(__apath__)

if parental_control:
	if __bLogging__ == "true":xbmc.log("With parental control")
	#START WITH NUMBER OF PLAYERS WINDOW
	mydisplay=dialog.KodifunLogin("splash-players.xml" , __apath__,'Default','720p')
	mydisplay.doModal()
	if __bLogging__ == "true":xbmc.log("SPY  =  " + str(mydisplay.ActionID))
	if (mydisplay.ActionID == 32204):
		mydisplay=dialog.KodifunLogin("splash-playersdata.xml" , __apath__,'Default','720p')
		mydisplay.doModal()
	if (mydisplay.ActionID == 32037):
		mydisplay=dialog.KodifunLogin("kodifun-gameboard.xml" , __apath__,'Default','720p')
		mydisplay.doModal()
	del mydisplay
else:
	if __bLogging__ == "true":xbmc.log("Without parental control")
	pass