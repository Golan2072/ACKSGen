# henchgenlib.py
# ACKS henchman and hireling generator data and rules library
# v0.2, February 9th, 2018.
# This is open source code, feel free to use it for any purpose.
# Contact the author at golan2072@gmail.com.

#import modules
import random
import string

def random_choice(list): #input list
	"""
	randomly chooses an element from a list.
	"""
	element=list[random.randint(0,len(list)-1)]
	return element #output randomly-selected element

def dice(n,sides): #inputs number of dice, sides per die
	"""
	die-rolling function
	"""
	die=0
	roll=0
	while die<n:
		roll=roll+random.randint(1,sides)
		die+=1
	return roll #outputs die roll result

def attribute_modifier(attribute): #input ability score
	"""
	generates attribute modifier from attribute
	"""
	modlib=[0, -3, -3, -3, -2, -2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3]
	return modlib[attribute] #output ability modifier
	
def sex_gen():
	"""
	sex-generating function
	"""
	roll=dice(1,6)
	if roll in [1, 2, 3]:
		return "male"
	elif roll in [4, 5, 6]:
		return "female"
	else:
		return "androgynous"

def race_gen(con):
	"""
	race-generating function
	"""
	roll=dice(1,6)
	if roll in [1, 2, 3, 4]:
		return "human"
	elif roll==5:
		return "elf"
	if roll==6 and con>=9:
		return "dwarf"
	else:
		return "human"
		
def name_gen(sex): #input character sex
	"""
	randomly chooses a character name from a list
	"""
	name=""
	if sex=="male":
		name=random_choice([\
		"Andrei",\
		"Alexander",\
		"Omar",\
		"Caleb",\
		"Marcus",\
		"Adar",\
		"Bal",\
		"Maoz",\
		"Borbus",\
		"Zadok",\
		"Alan",\
		"Ivan",\
		"Arad",\
		"Oran",\
		"Oleg",\
		"Alva",\
		"Sergei",\
		"Baruch",\
		"Barak",\
		"Ake",\
		"Arvid",\
		"Asger",\
		"Asmund",\
		"Audun",\
		"Balder",\
		"bard",\
		"Birger",\
		"Bjarke",\
		"Bjarni",\
		"Malcushius",\
		"Joseph",\
		"Vladimir",\
		"Ivar",\
		"Arne",\
		"Eirik",\
		"Geir",\
		"Gisle",\
		"Gunnar",\
		"Harald",\
		"Inge",\
		"Knut",\
		"Leif",\
		"Magnus",\
		"Olav",\
		"Rolf",\
		"Sigurd",\
		"Snorre",\
		"Steinar",\
		"Torstein",\
		"Trygve",\
		"Ulf",\
		"Valdemar",\
		"Vidar",\
		"Yngve",\
		"Abram",\
		"Alexander",\
		"Alexei",
		"Albert",\
		"Anatony",\
		"Andrei",\
		"Anton",\
		"Arkady",\
		"Arseny",\
		"Artyom",\
		"Artur",\
		"Afanasy",\
		"Bogdan",\
		"Boris",\
		"Vadim",\
		"Valentin",\
		"Valery",\
		"Veniamin",\
		"Viktor",\
		"Vitaly",\
		"Vlad",\
		"Vladimir",\
		"Vladislav",\
		"Vsevolod",\
		"Vyacheslav",\
		"Zoltan",\
		"Mikhail"])
		return name #output random male name
	elif sex=="female":
		name=random_choice([\
		"Anat",\
		"Alfhild",\
		"Asta",\
		"Astrid",\
		"Istrid",
		"Audhild",\
		"Bergljot",\
		"Brynhild",\
		"Aslaug",\
		"Aslog",\
		"Alvidla",\
		"Ase",\
		"Alva",
		"Hannah",\
		"Freydis",\
		"Gudrun",\
		"Gunhild",\
		"Gunnvor",\
		"Hilde",\
		"Ingrid",\
		"Ranghild",\
		"Ranveig",\
		"Sigrid",\
		"Sigrun",\
		"Siv",\
		"Solveig",\
		"Svanhild",\
		"Torhild",\
		"Torunn",\
		"Turid",\
		"Vigdis",\
		"Yngvild",\
		"Solveig",\
		"Sophie",\
		"Anna",\
		"Elizabeth",\
		"Isabel",\
		"Dina",\
		"Elena",\
		"Lyudmila",\
		"Larissa",\
		"Regina",\
		"Zara",\
		"Zarya",\
		"Kara",\
		"Ariella"])
		return name #output random female name
	else:	#in case of wrong input
		return "Tokay" #output placeholder

def charclass(STR, DEX, CON, INT, WIS, CHA, sex, race, level): #choses character class based on attributes, sex, and level
	attribute_list=[STR, DEX, CON, INT, WIS, CHA]
	profession="fighter"
	if level==0:
		profession="normal person"
	else:
		if race=="human":
			if STR==max(attribute_list):
				profession=random_choice(["fighter", "explorer"])
			elif DEX==max(attribute_list):
				profession=random_choice(["thief", "assassin"])
			elif CON==max(attribute_list):
				profession="fighter"
			elif INT==max(attribute_list):
				profession="mage"
			elif WIS==max(attribute_list) and sex=="male":
				profession="cleric"
			elif WIS==max(attribute_list) and sex=="female":
				random_choice(["bladedancer", "bladedancer", "cleric"])
			elif CHA==max(attribute_list):
				profession="bard"
			else:
				profession="fighter"
		elif race=="dwarf":
			if WIS==max(attribute_list):
				profession="craftpriest"
			else:
				profession="vaultguard"
		elif race=="elf":
			if INT==max(attribute_list):
				profession="spellsword"
			else:
				profession="nightblade"
		else:
			profession="fighter"
	return profession #returns chosen class	

def general_proficiency():
	"""
	generate general proficiencies
	"""
	return random_choice(["Alchemy", "Animal Husbandry", "Animal Training", "Art", "Bargaining", "Caving", "Collegiate Wizardry", "Craft", "Diplomacy", "Disguise", "Endurance", "Engineering", "Gambling", "Healing", "Intimidation", "Knowledge", "Labor", "Language", "Leadership", "Lip Reading", "Manual of Arms", "Mapping", "Military Strategy", "Mimicry", "Naturalism", "Navigation", "Performance", "Possession", "Riding", "Seafaring", "Seduction", "Siege Engineering", "Signalling", "Survival", "Theology", "Tracking", "Trapping"])

def assassin_proficiency():
	"""
	generate assassin proficiencies
	"""
	return random_choice(["Acrobatics", "Alchemy", "Alertness", "Arcane Dabbling", "Blind Fighting", "Bribery", "Cat Burglary", "Climbing", "Combat Reflexes", "Combat Trickery (disarm)", "Combat Trickery (incapacitate)", "Contortionism", "Disguise", "Eavesdropping", "Fighting Style", "Gambling", "Intimidation", "Mimicry", "Precise Shooting", "Running", "Seduction", "Skirmishing", "Skulking", "Sniping", "Swashbuckling", "Trap Finding", "Weapon Finesse", "Weapon Focus"])	

def bard_proficiency():
	"""
	generate bard proficiencies
	"""
	return random_choice(["Acrobatics", "Alchemy", "Alertness", "Arcane Dabbling", "Blind Fighting", "Bribery", "Cat Burglary", "Climbing", "Combat Reflexes", "Combat Trickery (disarm)", "Command", "Diplomacy", "Eavesdropping", "Elven Bloodline", "Fighting Style", "Healing", "Knowledge", "Language", "Leadership", "Lip Reading", "Magical Engineering", "Magical Music", "Mimicry", "Mystic Aura", "Performance", "Precise Shooting", "Prestidigitation", "Running", "Seduction", "Skirmishing", "Swashbuckling", "Weapon Finesse", "Weapon Focus"])
	
def bladedabcer_proficiency():
	"""
	generate bladedancer proficiencies
	"""
	return random_choice(["Acrobatics", "Apostasy", "Battle Magic", "Beast Friendship", "Combat Reflexes", "Combat Trickery (disarm)", "Combat Trickery (trip)", "Contemplation", "Diplomacy", "Divine Blessing", "Divine Health", "Fighting Style", "Laying on Hands", "Magical Music", "Martial Training", "Performance", "Prestidigitation", "Prophecy", "Quiet Magic", "Righteous Turning", "Running", "Seduction", "Skirmishing", "Swashbuckling", "Theology", "Unflappable Casting", "Weapon Finesse", "Weapon Focus"])
	
def cleric_proficiency():
	"""
	generate cleric proficiencies
	"""
	return random_choice(["Apostasy", "Battle Magic", "Beast Friendship", "Combat Trickery (force back)", "Combat Trickery (overrun)", "Combat Trickery (sunder)", "Command", "Contemplation", "Diplomacy", "Divine Blessing", "Divine Health", "Fighting Style", "Healing", "Knowledge (history)", "Laying on Hands", "Leadership", "Loremastery", "Magical Engineering", "Martial Training", "Prestidigitation", "Profession (judge)", "Prophecy", "Quiet Magic", "Righteous Turning", "Sensing Evil", "Sensing Power", "Theology", "Unflappable Casting", "Weapon Focus"])
	
def explorer_proficiency():
	"""
	generate explorer proficiencies
	"""
	return random_choice(["Alertness", "Ambushing", "Beast Friendship", "Blind Fighting", "Climbing", "Combat Reflexes", "Combat Trickery (disarm)", "Combat Trickery (knock down)", "Eavesdropping", "Endurance", "Fighting Style", "Land Surveying", "Mapping", "Mountaineering", "Naturalism", "Navigation", "Passing Without Trace", "Precise Shooting", "Riding", "Running", "Seafaring", "Skirmishing", "Sniping", "Survival", "Swashbuckling", "Trapping", "Weapon Finesse", "Weapon Focus"])

def fighter_proficiency():
	"""
	generate fighter proficiencies
	"""
	return random_choice(["Acrobatics", "Alertness", "Berserkergang", "Blind Fighting", "Combat Reflexes", "Combat Trickery (disarm)", "Combat Trickery (force back)", "Combat Trickery (knock down)", "Combat Trickery (sunder)", "Command", "Dungeon Bashing", "Endurance", "Fighting Style", "Gambling", "Intimidation", "Leadership", "Manual of Arms", "Military Strategy", "Precise Shooting", "Riding", "Running", "Siege Engineering", "Skirmishing", "Survival", "Swashbuckling", "Weapon Finesse", "Weapon Focus"])	

def mage_proficiency():
	"""
	generate mage proficiencies
	"""
	return random_choice(["Alchemy", "Battle Magic", "Beast Friendship", "Black Lore of Zahar", "Collegiate Wizardry", "Craft", "Diplomacy", "Elementalism", "Elven Bloodline", "Engineering", "Familiar", "Healing", "Illusion Resistance", "Knowledge", "Language", "Loremastery", "Magical Engineering", "Mapping", "Mystic Aura", "Naturalism", "Quiet Magic", "Performance", "Prestidigitation", "Profession", "Sensing Power", "Transmogrification", "Soothsaying", "Unflappable Casting"])
	
def thief_proficiency():
	"""
	generate thief proficiencies
	"""
	return random_choice(["Acrobatics", "Alertness", "Arcane Dabbling", "Blind Fighting", "Bribery", "Cat Burglary", "Combat Reflexes", "Combat Trickery (disarm)", "Combat Trickery (incapacitate)", "contortionism", "Diplomacy", "Fighting Style", "Gambling", "Intimidation", "Lip Reading", "Lockpicking", "Mapping", "Precise Shooting", "Riding", "Running", "Seafaring", "Skirmishing", "Skulking", "Sniping", "Swashbuckling", "Trap Finding", "Weapon Finesse", "Weapon Focus"])

def craftpriest_proficiency():
	"""
	generate craftpriest proficiencies
	"""
	return random_choice(["Alchemy", "Art", "Battle Magic", "Caving", "Collegiate Wizardry", "Contemplation", "Craft", "Diplomacy", "Divine Blessing", "Divine Health", "Dwarven Brewing", "Endurance", "Engineering", "Fighting Style", "Goblin-Slaying", "Healing", "Illusion Resistance", "Knowledge", "Laying on Hands", "Loremastery", "Magical Engineering", "Mapping", "Performance (chanting)", "Prestidigitation", "Profession (judge)", "Prophecy", "Quiet Magic", "Righteous Turning", "Sensing Evil", "Siege Engineering", "Theology", "Unflappable Casting", "Weapon Focus"])

def vaultguard_proficiency():
	"""
	generate vaultguard proficiencies
	"""
	return random_choice(["Alertness", "Berserkergang", "Blind Fighting", "Caving", "Combat Reflexes", "Combat Trickery (force back)", "Combat Trickery (knock down)", "Combat Trickery (overrun)", "Combat Trickery (sunder)", "Combat Trickery (wrestle)", "Command", "Craft", "Dungeon Bashing", "Dwarven Brewing", "Endurance", "Engineering", "Fighting Style", "Gambling", "Goblin-Slaying", "Illusion Resistance", "Intimidation", "Land Surveying", "Leadership", "Mapping", "Manual of Arms", "Military Strategy", "Mountaineering", "Siege Engineering", "Weapon Focus"])
	
def nightblade_proficiency():
	"""
	generate nightblade proficiencies
	"""
	return random_choice(["Alchemy", "Alertness", "Battle Magic", "Beast Friendship", "Black Lore of Zahar", "Blind Fighting", "Combat Reflexes", "Combat Trickery (disarm)", "Combat Trickery (incapacitate)", "Contortionism", "Elementalism", "Familiar", "Fighting Style", "Intimidation", "Magical Engineering", "Mystic Aura", "Passing Without Trace", "Precise Shooting", "Prestidigitation", "Quiet Magic", "Running", "Sensing Power", "Skirmishing", "Skulking", "Sniping", "Swashbuckling", "Unflappable Casting", "Trap Finding", "Wakefulness", "Weapon Focus", "Weapon Finesse"])

def spellsword_proficiency():
	"""
	generate spellsword proficiencies
	"""
	return random_choice(["Acrobatics", "Alertness", "Battle Magic", "Beast Friendship", "Black Lore of Zahar", "Blind Fighting", "Combat Reflexes", "Combat Trickery (disarm)", "Combat Trickery (knock down)", "Command", "Elementalism", "Familiar", "Fighting Style", "Leadership", "Loremastery", "Magical Engineering", "Magical Music", "Mystic Aura", "Naturalism", "Passing Without Trace", "Quiet Magic", "Precise Shooting", "Prestidigitation", "Running", "Sensing Power", "Skirmishing", "Soothsaying", "Swashbuckler", "Unflappable Casting", "Wakefulness", "Weapon Focus", "Weapon Finesse"])
	
def genprofgen(level, intmod): #input level and intelligence modifier
	"""
	generates general proficiencies
	"""
	proflist=[]
	if level==0:
			for i in range (0, 4):
				proflist.append(general_proficiency())
			if intmod>=1:
				for i in range (0, intmod):
					proflist.append(general_proficiency())
	else:
		if intmod>=1:
			for i in range (0, intmod+1):
				proflist.append(general_proficiency())
		else:
			proflist=[general_proficiency()]
	return proflist #output general proficiency list
	
def profgen(intmod, level, cclass): #input character's intelligence modifier, level, and character class
	"""
	generate proficiency list
	"""
	proflist=genprofgen(level, intmod)
	if cclass=="assassin":
		proflist.append (assassin_proficiency())
	elif cclass=="bard":
		proflist.append (bard_proficiency())
	elif cclass=="bladedancer":
		proflist.append (bladedancer_proficiency())
	elif cclass=="cleric":
		proflist.append (cleric_proficiency())
	elif cclass=="explorer":
		proflist.append (explorer_proficiency())
	elif cclass=="fighter":
		proflist.append (fighter_proficiency())
	elif cclass=="mage":
		proflist.append (mage_proficiency())
	elif cclass=="thief":
		proflist.append (thief_proficiency())
	elif cclass=="craftpriest":
		proflist.append (craftpriest_proficiency())
	elif cclass=="vaultguard":
		proflist.append (vaultguard_proficiency())
	elif cclass=="nightblade":
		proflist.append (nightblade_proficiency())
	elif cclass=="spellsword":
		proflist.append (spellsword_proficiency())
	return proflist #output proficiency list

def hp_gen(cclass, conmod, level): #input character class, constitution modifier, and level
	"""
	hit point generator
	"""
	if level==0:
		hp=dice(1, 6)+conmod
	else:
		if cclass in ["fighter", "vaultguard"]:
			hp=dice(level, 8)+conmod
		elif cclass in ["mage", "thief"]:
			hp=dice(level, 4)+conmod
		elif cclass in ["assassin", "cleric", "bard", "bladedancer", "explorer", "craftpriest", "spellsword", "nightblade"]:
			hp=dice(level, 6)+conmod
		else:
			hp=1+conmod
	if hp<1:
		hp=1
	return hp #output hit points

def weapon_gen (cclass): #input character class
	"""
	weapon generation
	"""
	if cclass in ["fighter", "spellsword"]:
		return random_choice(["Battle Axe", "Great Axe", "Hand Axe","Arbalest", "Crossbow", "Composite Bow", "Longbow", "Shortbow", "Club", "Flail", "Mace", "Morning Star", "Warhammer", "Javelin", "Pole Arm", "Spear", "Dagger", "Short Sword", "Sword", "Two-Handed Sword", "Staff", "Whip"])
	if cclass=="mage":
		return random_choice(["Staff", "Club", "Dagger", "Dart"])
	if cclass=="cleric":
		return random_choice(["Warhammer", "Mace", "Club", "Morning Star", "Staff", "Sling"])
	if cclass in ["thief", "bard", "explorer", "nightblade"]:
		return random_choice(["Battle Axe", "Hand Axe", "Arbalest", "Crossbow", "Composite Bow", "Longbow", "Shortbow", "Club", "Flail", "Sap", "Mace", "Warhammer", "Javelin", "Spear", "Dagger", "Short Sword", "Sword", "Whip"])
	if cclass=="assassin":
		return random_choice(["Hand Axe", "Hand Axe", "Arbalest", "Crossbow", "Crossbow", "Composite Bow", "Longbow", "Shortbow", "Dagger", "Dagger", "Dagger", "Dagger", "Dagger", "Short Sword", "Short Sword", "Short Sword", "Sword"])
	if cclass=="bladedancer":
		return random_choice(["Battle Axe", "Great Axe", "Hand Axe", "Dagger", "Sword", "Sword", "Sword", "Shortsword", "Shortsword", "Two-Handed Sword", "Two-Handed Sword"])
	if cclass=="vaultguard":
		return random_choice(["Battle Axe", "Battle Axe", "Battle Axe", "Great Axe", "Great Axe", "Great Axe", "Hand Axe", "Hand Axe", "Hand Axe", "Hand Axe", "Arbalest", "Crossbow", "Composite Bow", "Shortbow", "Club", "Flail", "Mace", "Warhammer", "Warhammer", "Warhammer", "Javelin", "Spear", "Dagger", "Short Sword", "Short Sword", "Whip"])
	if cclass=="craftpriest":
		return random_choice(["Battle Axe", "Great Axe", "Hand Axe", "Flail", "Mace", "Morning Star", "Warhammer"])
