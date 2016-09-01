import xbmc
import xbmcaddon
__settings__ = xbmcaddon.Addon('script.kodifun.game')
__language__ = __settings__.getLocalizedString
__language__(30204)              # this will return localized string from resources/language/<name_of_language>/strings.xml
#__settings__.getSetting( "foo" ) # this will return "foo" setting value 
#__settings__.setSetting( "foo" ) # this will set "foo" setting value
#__settings__.openSettings()      # this will open settings window
 
xbmc.log("KodiFun KodiFunAttrib loaded")

def setAttribute():
	"""Generate value for an attribute.
	At the moment all attributes are set to 0
	"""
	attrib = 0
	xbmc.log("KodiFun KodiFunAttrib setAttribute loaded")

	return attrib

def makeDice1Assign():
	dice_assignments = {}
	dice_assignments["1"]= __language__(32101)
	dice_assignments["2"]= __language__(32102)
	dice_assignments["3"]= __language__(32103)
	dice_assignments["4"]= __language__(32104)
	dice_assignments["5"]= __language__(32105)
	dice_assignments["6"]= __language__(32106)

	return dice_assignments

def makeDice2Assign():
	dice_assignments = {}
	dice_assignments["1"]= __language__(32111)
	dice_assignments["2"]= __language__(32112)
	dice_assignments["3"]= __language__(32113)
	dice_assignments["4"]= __language__(32114)
	dice_assignments["5"]= __language__(32115)
	dice_assignments["6"]= __language__(32116)

	return dice_assignments
	
def makeAttrib():
	xbmc.log("KodiFun KodiFunAttrib makeAttrib loaded")
	#---Make dictionary of attributes
	attrib_dict = {}    
	
	#---Get values for core attributes
	attrib_dict["stren"] = setAttribute()			#strength
	attrib_dict["intel"] = setAttribute()			#intelligence
	attrib_dict["will"] = setAttribute()			#willpower
	attrib_dict["charisma"] = setAttribute()		#charisma
	attrib_dict["build"] = setAttribute()			#build
	attrib_dict["dex"] = setAttribute()				#dexterity
	attrib_dict["age"] = setAttribute()				#age

	return attrib_dict
	
def makeAttribGender(gender,attrib_dict):
	xbmc.log("KodiFun KodiFunAttrib makeAttribGender loaded")
	if gender == "female":
		attrib_dict["gender"] = __language__(32064)
		attrib_dict["feet1"] = __language__(32070)
		attrib_dict["feet2"] = __language__(32071)
		attrib_dict["waist1"] = __language__(32072)
		attrib_dict["waist2"] = __language__(32073)
		attrib_dict["chest1"] = __language__(32074)
		attrib_dict["chest2"] = __language__(32075)
	elif gender == "male":
		attrib_dict["gender"] = __language__(32063)
		attrib_dict["feet1"] = __language__(32080)
		attrib_dict["feet2"] = __language__(32081)
		attrib_dict["waist1"] = __language__(32082)
		attrib_dict["waist2"] = __language__(32083)
		attrib_dict["chest1"] = __language__(32084)
		attrib_dict["chest2"] = __language__(32085)
	return attrib_dict

def printCharacter(self):
	xbmc.log("KodiFun Character has the following attributes:")
	for key, value in self.attrib.iteritems() :
		xbmc.log("KodiFun Key " + key + " : " + str(value))

def setPlayerData(self):
	self.getControl(32060).setText(str(__settings__.getSetting(str(32301 + self.counter * self.offsetPlayerData))))
	self.getControl(32061).setText(str(__settings__.getSetting(str(32302 + self.counter * self.offsetPlayerData))))
	if(__settings__.getSetting(str(32303 + self.counter * self.offsetPlayerData)) == "1"):
		self.getControl(32063).setSelected(1)
	else:
		self.getControl(32064).setSelected(1)
	if(__settings__.getSetting(str(32304 + self.counter * self.offsetPlayerData)) == "1"):
		self.getControl(32065).setSelected(1)
	if(__settings__.getSetting(str(32305 + self.counter * self.offsetPlayerData)) == "1"):
		self.getControl(32066).setSelected(1)
	self.getControl(32222).setLabel(str(__language__(32222)+ " " + str(self.counter + 1)))
	pass

def setGameBoard(self):
	xbmc.log("KodiFun KodiFunAttrib setGameBoard Loaded" + str(self.players) + str(self.counter))
	self.counter = 0
	for self.counter in range(0,4):
		xbmc.log("KodiFun KodiFunAttrib setGameBoard Loaded" + str(self.players) + str(self.counter))
		self.getControl(32301 + self.counter * self.offsetPlayerData).setLabel(str(__settings__.getSetting(str(32301 + self.counter * self.offsetPlayerData))))
		self.getControl(32302 + self.counter * self.offsetPlayerData).setLabel(str(__settings__.getSetting(str(32302 + self.counter * self.offsetPlayerData))))
		if self.players > self.counter:
			self.getControl(32300 + self.counter * self.offsetPlayerData).setVisible(1)
		else:
			xbmc.log("KodiFun KodiFunAttrib setGameBoard Loaded" + str(self.players) + str(self.counter))
			self.getControl(32300 + self.counter * self.offsetPlayerData).setVisible(0)
		xbmc.log("KodiFun image selected is " + str(__settings__.getSetting(str(32303 + self.counter * self.offsetPlayerData))) + str(self.counter + 1) + "PlayerImage.png")
		self.getControl(32306 + self.counter * self.offsetPlayerData).setImage(str(__settings__.getSetting(str(32303 + self.counter * self.offsetPlayerData))) + str(self.counter + 1) + "PlayerImage.png")
	pass
