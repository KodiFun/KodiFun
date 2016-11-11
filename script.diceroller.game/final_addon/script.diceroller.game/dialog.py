#!/usr/bin/python
# -*- coding: utf-8 -*-
# from xbmcswift2 
import xbmc, xbmcgui
import xbmcvfs
# import kodifunattrib
import random
# import diceroller
import xbmcaddon
__addon__     = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__settings__  = xbmcaddon.Addon('script.kodifun.game')
__language__  = __settings__.getLocalizedString
__settings__.getSetting( "foo" ) # this will return "foo" setting value 
__bLogging__  =__settings__.getSetting("32004")


#SKIN BUTTONS

CTRL_ID_OK = 32033
CTRL_ID_CANCEL = 32034
CTRL_ID_REFRESH = 300
EXIT_DIALOG = 301

#KEYBOARD KEYS

ACTION_KEY_LEFT=1
ACTION_KEY_RIGHT=2
ACTION_KEY_UP=3
ACTION_KEY_DOWN=4
ACTION_KEY_BACKSPACE = 8
ACTION_KEY_SPACE=12
ACTION_KEY_TAB=18
ACTION_PREVIOUS_MENU = (10,92)

#CEC REMOTE KEYS
#https://github.com/xbmc/xbmc/blob/master/xbmc/input/ButtonTranslator.cpp
# CEC_KEY_UP=166
# CEC_KEY_DOWN=167
# CEC_KEY_LEFT=168
# CEC_KEY_RIGHT=169

class KodifunLogin(xbmcgui.WindowXML):

    def __init__(self, strXMLname, strFallbackPath, defaultSkin='Default',
                 forceFallback=False):
		# def __init__( self, *args, **kwargs ):
		# Changing the three varibles passed won't change, anything
		# Doing strXMLname = "bah.xml" will not change anything.
		# don't put GUI sensitive stuff here (as the xml hasn't been read yet
		# Idea to initialize your variables here
		self.ControlListIndex=0
		self.ActionID=0
		self.input_text = ''
		self.username = ''
		self.password = ''
		self.players = int(__settings__.getSetting("32003"))
		self.counter = 0
		self.offsetPlayerData = 20
		self.SkinXML = strXMLname
		self.PreviousPlayer = 0
		self.currentplayer = random.randint(1,self.players)
		self.assignment = ""
		self._ok = False
		self.Sex = 'M'
		self.SexChoiceMale=0
		self.dice1=0
		self.dice2=0
		self.dice3=0
		self.dice4=0
		# self.player=kodifunattrib.setPlayerData(self)
		self.attrib=kodifunattrib.makeAttrib()
		self.attrib=kodifunattrib.makeAttribGender("male",self.attrib)
		print kodifunattrib.printCharacter(self)
		# if(strXMLname == "splash-players.xml)":
		if __bLogging__ == "true":xbmc.log("SPY on __init__ " +str(self.players) + " " + strXMLname)
		# self.attribs = AttributeGenerator.makeAttrib()
		### make the list
		# self.ctl = xbmcgui.ControlList(210, 100, 335, 360, 'font14')
		# self.addControl(self.ctl)
		# self.setFocus(32203)

		#self.AddControl(self.statlist)
		# self.ListItem = xbmcgui.ListItem(label=str('philip', IconImage = "user.png")
		imgurl = 'special://temp/baidu_captcha.jpg'
        # super(MyFirstWinXML, self).__init__(self, *args)

    # def __del__(self):
        # tmp_imgfile = self._tmp_imgfile
        # if xbmcvfs.exists(self._tmp_imgfile):
            # try:
                # xbmcvfs.delete(tmp_imgfile)
            # except:
                # pass
		
    def _download_img(self):
        #imgdata = utils.fetch_url(self._imgurl, timeout=10)
        #xbmcvfs.File(self._tmp_imgfile, 'w').write(imgdata)
		pass

    def onInit(self):
		 if __bLogging__ == "true":xbmc.log("SPY onInit(self) " +str(xbmcgui.getCurrentWindowId()) + " " + self.SkinXML)
		 if(self.SkinXML == "splash-players.xml"):
			self.getControl(32203).setText(str(self.players))
			self.ListControls=[32203,32034,32204]
			self.setFocusId(32203)
		 elif(self.SkinXML == "splash-playersdata.xml"):
			self.getControl(32060).setText(str(__settings__.getSetting(str(32301 + self.counter * self.offsetPlayerData))))
			self.getControl(32061).setText(str(__settings__.getSetting(str(32302 + self.counter * self.offsetPlayerData))))
			self.ListControls=[32060,32061,32063,32064,32065,32066,32034,32037]
			self.setFocusId(32060)
			if(__settings__.getSetting(str(32303 + self.counter * self.offsetPlayerData)) == "1"):
				self.getControl(32063).setSelected(1)
			else:
				self.getControl(32064).setSelected(1)
			if(__settings__.getSetting(str(32304 + self.counter * self.offsetPlayerData)) == "1"):
				self.getControl(32065).setSelected(1)
			if(__settings__.getSetting(str(32305 + self.counter * self.offsetPlayerData)) == "1"):
				self.getControl(32066).setSelected(1)
			self.getControl(32222).setLabel(str(__language__(32222)+ " " + str(self.counter + 1)))
		 elif(self.SkinXML == "kodifun-gameboard.xml"):
			self.ListControls=[32034,32037]
			if __bLogging__ == "true":xbmc.log("SPY onInit2(self) " +str(xbmcgui.getCurrentWindowId()) + " " + self.SkinXML)
			self.setFocusId(32039)
			kodifunattrib.setGameBoard(self)
			self.counter=0
			for self.counter in range(0,4):
				self.getControl(32301 + self.counter * self.offsetPlayerData).setLabel(str(__settings__.getSetting(str(32301 + self.counter * self.offsetPlayerData))))
				self.getControl(32302 + self.counter * self.offsetPlayerData).setLabel(str(__settings__.getSetting(str(32302 + self.counter * self.offsetPlayerData))))
			if self.players > self.counter:
				self.getControl(32300 + self.counter * self.offsetPlayerData).setVisible(1)
			else:
				self.getControl(32300 + self.counter * self.offsetPlayerData).setVisible(0)
				if __bLogging__ == "true":xbmc.log("KodiFun image selected is " + str(__settings__.getSetting(str(32303 + self.counter * self.offsetPlayerData))) + str(self.counter + 1) + "PlayerImage.png")
				self.getControl(32306 + self.counter * self.offsetPlayerData).setImage(str(__settings__.getSetting(str(32303 + self.counter * self.offsetPlayerData))) + str(self.counter + 1) + "PlayerImage.png")
		
		 pass
    def prevControl(self, action):
		if self.ControlListIndex <= 0: 
			self.ControlListIndex = len(self.ListControls)-1
		else:
			self.ControlListIndex = self.ControlListIndex -1
		if __bLogging__ == "true":xbmc.log(str(len(self.ListControls)) + " prevControl " + str(self.ListControls[self.ControlListIndex]) + " key: " + str(self.ControlListIndex))
		self.setFocusId(self.ListControls[self.ControlListIndex])
		pass
    def nextControl(self, action):
		if self.ControlListIndex >= len(self.ListControls)-1: 
			self.ControlListIndex = 0
		else:
			self.ControlListIndex = self.ControlListIndex +1
		if __bLogging__ == "true":xbmc.log(str(len(self.ListControls)) + " nextControl " + str(self.ListControls[self.ControlListIndex]) + " key: " + str(self.ControlListIndex))
		self.setFocusId(self.ListControls[self.ControlListIndex])


		pass

    def get_text(self):
        if self._ok:
            return self.input_text

    def onAction(self, action):
        # Same as normal python Windows.
        if __bLogging__ == "true":xbmc.log("onAction =" + str(action.getId()) + "/" )
        if action.getId() == ACTION_KEY_LEFT :
            if __bLogging__ == "true":xbmc.log("onAction ACTION_KEY_LEFT=" + str(action.getId()) + "/" )
            self.prevControl(self)
            return
        if action.getId() == ACTION_KEY_RIGHT:
            if __bLogging__ == "true":xbmc.log("onAction ACTION_KEY_RIGHT=" + str(action.getId()) + "/" )
            self.nextControl(self)
            return
        if action.getId() == ACTION_KEY_DOWN :
            if __bLogging__ == "true":xbmc.log("onAction ACTION_KEY_DOWN=" + str(action.getId()) + "/" )
            self.prevControl(self)
            return
        if action.getId() == ACTION_KEY_UP:
            if __bLogging__ == "true":xbmc.log("onAction ACTION_KEY_UP=" + str(action.getId()) + "/" )
            self.nextControl(self)
            return
		# CEC remote
        if action.GetButtonCode() == ACTION_MOVE_LEFT  :
            if __bLogging__ == "true":xbmc.log("onAction ACTION_MOVE_LEFT =" + str(action.getId()) + "/" )
            self.prevControl(self)
            return
        if action.getId() == ACTION_MOVE_RIGHT :
            if __bLogging__ == "true":xbmc.log("onAction ACTION_MOVE_LEFT =" + str(action.getId()) + "/" )
            self.nextControl(self)
            return
        if action.GetButtonCode() == ACTION_MOVE_UP  :
            if __bLogging__ == "true":xbmc.log("onAction ACTION_MOVE_LEFT =" + str(action.getId()) + "/" )
            self.prevControl(self)
            return
        if action.getId() == ACTION_MOVE_DOWN :
            if __bLogging__ == "true":xbmc.log("onAction ACTION_MOVE_LEFT =" + str(action.getId()) + "/" )
            self.nextControl(self)
            return
        if action in ACTION_PREVIOUS_MENU:
            return

        if action == EXIT_DIALOG:
            return

    def onClick(self, controlID):
        """
            Notice: onClick not onControl
            Notice: it gives the ID of the control not the control object
        """
        self.ActionID = controlID
        if CTRL_ID_CANCEL == controlID:
            self.close()
        elif CTRL_ID_OK == controlID:
             if (len(self.username)>4) & (len(self.password)>4):
                 if __bLogging__ == "true":xbmc.log("KodiFun Lenght is larger")
             else:
                  if __bLogging__ == "true":xbmc.log("KodiFun Lenght is to short")
             if __bLogging__ == "true":xbmc.log("KodiFun " + self.username)
             # self.close()
        elif controlID == 32011:
             self.username = str(self.getControl(controlID).getText())
             if __bLogging__ == "true":xbmc.log("KodiFun " + self.username)
        elif controlID == 32012:
             self.password = str(self.getControl(controlID).getText())
             if __bLogging__ == "true":xbmc.log("KodiFun " + self.password)
        elif controlID == 32037:
             if(int(self.counter)  <= int(self.players - 2)):
                 self.counter = self.counter+1
                 kodifunattrib.setPlayerData(self)
                 if __bLogging__ == "true":xbmc.log("Info for next player=" + str(self.counter) + "/" + str(self.players))
             else:
                 if __bLogging__ == "true":xbmc.log("Info Complete close screen=" + str(self.counter) + "/" + str(self.players))
                 self.counter = 0
                 self.close()
        elif controlID == 32039:
             self.dice1 = random.randint(1, 6)
             self.getControl(32046).setLabel("[B]" + str(self.dice1) + "[/B]")
             self.getControl(32048).setImage("\set1\l" + str(self.dice1) + ".png")
             self.dice2 = random.randint(1, 6)
             self.getControl(32045).setLabel("[B]" + str(self.dice2) +"[/B]")
             self.getControl(32047).setImage("\set1\l" + str(self.dice2) + ".png")
             if __bLogging__ == "true":xbmc.log("ROLL DICE dice 1= " + str(self.dice1) + " dice 2 = "+ str(self.dice2))
             # Switch to next player
             self.PreviousPlayer = self.currentplayer
             if(self.currentplayer == self.players):
                 self.currentplayer = 1
             else:
                 self.currentplayer = self.currentplayer + 1
             self.getControl(32092).setLabel("[B]" + str(self.currentplayer) + "[/B]")
             # set the assignment
             # self.assignment = __language__(32094).getLabel()
             self.assignment = "Player " + str(self.PreviousPlayer) + " " + __language__(32100 + self.dice1) + " the " + __language__(32110 + self.dice2) + " of Player " + str(self.currentplayer) + " "
             self.getControl(32094).setLabel("[B]" + str(self.assignment) +"[/B]")
             if __bLogging__ == "true":xbmc.log(" INFO " + self.assignment)
        #set player name
        elif controlID == 32060:
             __settings__.setSetting( id=str(32301 + self.counter * self.offsetPlayerData) , value=str(self.getControl(32060).getText()))
             if __bLogging__ == "true":xbmc.log(" INFO " + self.assignment)
		#set player age
        elif controlID == 32061:
             __settings__.setSetting( id=str(32302 + self.counter * self.offsetPlayerData) , value=str(self.getControl(32061).getText()))
             if __bLogging__ == "true":xbmc.log(" INFO " + self.assignment)
		#set player gender to male
        elif controlID == 32063:
             self.SexChoiceMale = self.getControl(32063).isSelected()
             if(self.SexChoiceMale == 0):
                 self.getControl(32064).setSelected(1)
                 self.getControl(32063).setSelected(0)
             else:
                 self.getControl(32064).setSelected(0)
                 self.getControl(32063).setSelected(1)
             if __bLogging__ == "true":xbmc.log("KodiFun SexChoiceMale " + str(self.SexChoiceMale))
             __settings__.setSetting( id=str(32303 + self.counter * self.offsetPlayerData) , value=str(self.SexChoiceMale))
		#set player gender to female
        elif controlID == 32064:
             self.SexChoiceMale != self.getControl(32064).isSelected()
             if(self.getControl(32064).isSelected() == 0):
                 self.getControl(32063).setSelected(1)
                 self.getControl(32064).setSelected(0)
                 self.SexChoiceMale = self.getControl(32063).isSelected()
             else:
                 self.getControl(32063).setSelected(0)
                 self.getControl(32064).setSelected(1)
                 self.SexChoiceMale = self.getControl(32063).isSelected()
             __settings__.setSetting( id=str(32303 + self.counter * self.offsetPlayerData) , value=str(self.SexChoiceMale))
             if __bLogging__ == "true":xbmc.log("KodiFun SexChoiceMale " + str(self.SexChoiceMale))
		# Limit interactions to male
        elif controlID == 32065:
             __settings__.setSetting( id=str(32304 + self.counter * self.offsetPlayerData) , value=str(self.getControl(32065).isSelected()))
             if __bLogging__ == "true":xbmc.log("KodiFun Limit interactions to male = " + str(self.getControl(32065).isSelected()))
		# Limit interactions to female
        elif controlID == 32066:
             __settings__.setSetting( id=str(32305 + self.counter * self.offsetPlayerData) , value=str(self.getControl(32066).isSelected()))
             if __bLogging__ == "true":xbmc.log("KodiFun Limit interactions to female = " + str(self.getControl(32066).isSelected()))
        elif controlID == 32203:
             self.players = self.getControl(32203).getText()
             if __bLogging__ == "true":xbmc.log("SPY Number of players=" + str(self.players))
             if (int(self.players) < 2):
                 xbmcgui.Dialog().ok(__addonname__, __language__(32205))
                 if __bLogging__ == "true":xbmc.log("SPY It will be lonely alone")
                 self.getControl(32204).setEnabled(0)
             elif(int(self.players) > 4):
                 if __bLogging__ == "true":xbmc.log("SPY More then 4 is not possible yet")
                 xbmcgui.Dialog().ok(__addonname__, __language__(32206))
                 self.getControl(32204).setEnabled(0)
             elif(int(self.players) >= 2 & int(self.players) <= 4):
                 if __bLogging__ == "true":xbmc.log("SPY In range show button")
                 self.getControl(32204).setEnabled(1)
                 __settings__.setSetting( id="32400" , value=str(self.players))
             # self.username = str(self.getControl(32011).getText())
             if __bLogging__ == "true":xbmc.log("SPY Number of players=" + str(self.players))
        elif controlID == 32204:
             self.close()
        elif controlID == 32800:
             for self.counter in range(0,4):
                 self.getControl(32301 + self.counter * self.offsetPlayerData).setLabel(str(__settings__.getSetting(str(32301 + self.counter * self.offsetPlayerData))))
                 self.getControl(32302 + self.counter * self.offsetPlayerData).setLabel(str(__settings__.getSetting(str(32302 + self.counter * self.offsetPlayerData))))
                 if self.players > self.counter:
                     self.getControl(32300 + self.counter * self.offsetPlayerData).setVisible(1)
                 else:
                     self.getControl(32300 + self.counter * self.offsetPlayerData).setVisible(0)
                 if __bLogging__ == "true":xbmc.log("KodiFun image selected is " + str(__settings__.getSetting(str(32303 + self.counter * self.offsetPlayerData))) + str(self.counter + 1) + "PlayerImage.png")
                 self.getControl(32306 + self.counter * self.offsetPlayerData).setImage(str(__settings__.getSetting(str(32303 + self.counter * self.offsetPlayerData))) + str(self.counter + 1) + "PlayerImage.png")
        input_text = self.input_text
        if __bLogging__ == "true":xbmc.log("KodiFun " + str(controlID))

    def onFocus(self, controlID):
         # self.getControl(32204).setEnabled(0)
        WINDOW = xbmcgui.Window(xbmcgui.getCurrentWindowId())
        if __bLogging__ == "true":xbmc.log("SPY Window " +str(xbmcgui.getCurrentWindowId()))
        self.playmates = WINDOW.getProperty("playmates")
        if WINDOW.getProperty("playmates") != "":
            # try:
             self.players = WINDOW.getProperty("playmates")
        if __bLogging__ == "true":xbmc.log("SPY retrieved property" +str(self.playmates))
    pass
    """
    Character creation below this line
    """
    

