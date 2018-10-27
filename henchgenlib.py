# henchgenlib.py
# ACKS henchman and hireling generator data and rules library
# v0.25, February 11th, 2018.
# This is open source code, feel free to use it for any purpose.
# Contact the author at golan2072@gmail.com.

#import modules
import random
import string
from RPG import stellagama

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
	roll=stellagama.dice(1,6)
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
	roll=stellagama.dice(1,6)
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
		return stellagama.random_line("RPG/malenames.txt") #output random male name
	elif sex=="female":
		return stellagama.random_line("RPG/femalenames.txt") #output random female name
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
				profession=stellagama.random_choice(["fighter", "explorer"])
			elif DEX==max(attribute_list):
				profession=stellagama.random_choice(["thief", "assassin"])
			elif CON==max(attribute_list):
				profession="fighter"
			elif INT==max(attribute_list):
				profession="mage"
			elif WIS==max(attribute_list) and sex=="male":
				profession="cleric"
			elif WIS==max(attribute_list) and sex=="female":
				stellagama.random_choice(["bladedancer", "bladedancer", "cleric"])
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
	return stellagama.random_choice(["Alchemy", "Animal Husbandry", "Animal Training", "Art", "Bargaining", "Caving", "Collegiate Wizardry", "Craft", "Diplomacy", "Disguise", "Endurance", "Engineering", "Gambling", "Healing", "Intimidation", "Knowledge", "Labor", "Language", "Leadership", "Lip Reading", "Manual of Arms", "Mapping", "Military Strategy", "Mimicry", "Naturalism", "Navigation", "Performance", "Possession", "Riding", "Seafaring", "Seduction", "Siege Engineering", "Signalling", "Survival", "Theology", "Tracking", "Trapping"])
	
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

def classprof(level, cclass): #input character level
	"""
	generate class proficiencies
	"""
	proflist=[]
	if cclass=="assassin":
		profs=["Acrobatics", "Alchemy", "Alertness", "Arcane Dabbling", "Blind Fighting", "Bribery", "Cat Burglary", "Climbing", "Combat Reflexes", "Combat Trickery (disarm)", "Combat Trickery (incapacitate)", "Contortionism", "Disguise", "Eavesdropping", "Fighting Style", "Gambling", "Intimidation", "Mimicry", "Precise Shooting", "Running", "Seduction", "Skirmishing", "Skulking", "Sniping", "Swashbuckling", "Trap Finding", "Weapon Finesse", "Weapon Focus"]
	if cclass=="bard":
		profs=["Acrobatics", "Alchemy", "Alertness", "Arcane Dabbling", "Blind Fighting", "Bribery", "Cat Burglary", "Climbing", "Combat Reflexes", "Combat Trickery (disarm)", "Command", "Diplomacy", "Eavesdropping", "Elven Bloodline", "Fighting Style", "Healing", "Knowledge", "Language", "Leadership", "Lip Reading", "Magical Engineering", "Magical Music", "Mimicry", "Mystic Aura", "Performance", "Precise Shooting", "Prestidigitation", "Running", "Seduction", "Skirmishing", "Swashbuckling", "Weapon Finesse", "Weapon Focus"]
	if cclass=="bladedancer":
		profs=["Acrobatics", "Apostasy", "Battle Magic", "Beast Friendship", "Combat Reflexes", "Combat Trickery (disarm)", "Combat Trickery (trip)", "Contemplation", "Diplomacy", "Divine Blessing", "Divine Health", "Fighting Style", "Laying on Hands", "Magical Music", "Martial Training", "Performance", "Prestidigitation", "Prophecy", "Quiet Magic", "Righteous Turning", "Running", "Seduction", "Skirmishing", "Swashbuckling", "Theology", "Unflappable Casting", "Weapon Finesse", "Weapon Focus"]
	if cclass=="cleric":
		profs=["Apostasy", "Battle Magic", "Beast Friendship", "Combat Trickery (force back)", "Combat Trickery (overrun)", "Combat Trickery (sunder)", "Command", "Contemplation", "Diplomacy", "Divine Blessing", "Divine Health", "Fighting Style", "Healing", "Knowledge (history)", "Laying on Hands", "Leadership", "Loremastery", "Magical Engineering", "Martial Training", "Prestidigitation", "Profession (judge)", "Prophecy", "Quiet Magic", "Righteous Turning", "Sensing Evil", "Sensing Power", "Theology", "Unflappable Casting", "Weapon Focus"]
	if cclass=="explorer":
		profs=["Alertness", "Ambushing", "Beast Friendship", "Blind Fighting", "Climbing", "Combat Reflexes", "Combat Trickery (disarm)", "Combat Trickery (knock down)", "Eavesdropping", "Endurance", "Fighting Style", "Land Surveying", "Mapping", "Mountaineering", "Naturalism", "Navigation", "Passing Without Trace", "Precise Shooting", "Riding", "Running", "Seafaring", "Skirmishing", "Sniping", "Survival", "Swashbuckling", "Trapping", "Weapon Finesse", "Weapon Focus"]
	if cclass=="fighter":
		profs=["Acrobatics", "Alertness", "Berserkergang", "Blind Fighting", "Combat Reflexes", "Combat Trickery (disarm)", "Combat Trickery (force back)", "Combat Trickery (knock down)", "Combat Trickery (sunder)", "Command", "Dungeon Bashing", "Endurance", "Fighting Style", "Gambling", "Intimidation", "Leadership", "Manual of Arms", "Military Strategy", "Precise Shooting", "Riding", "Running", "Siege Engineering", "Skirmishing", "Survival", "Swashbuckling", "Weapon Finesse", "Weapon Focus"]
	if cclass=="mage":
		profs=["Alchemy", "Battle Magic", "Beast Friendship", "Black Lore of Zahar", "Collegiate Wizardry", "Craft", "Diplomacy", "Elementalism", "Elven Bloodline", "Engineering", "Familiar", "Healing", "Illusion Resistance", "Knowledge", "Language", "Loremastery", "Magical Engineering", "Mapping", "Mystic Aura", "Naturalism", "Quiet Magic", "Performance", "Prestidigitation", "Profession", "Sensing Power", "Transmogrification", "Soothsaying", "Unflappable Casting"]
	if cclass=="thief":
		profs=["Acrobatics", "Alertness", "Arcane Dabbling", "Blind Fighting", "Bribery", "Cat Burglary", "Combat Reflexes", "Combat Trickery (disarm)", "Combat Trickery (incapacitate)", "contortionism", "Diplomacy", "Fighting Style", "Gambling", "Intimidation", "Lip Reading", "Lockpicking", "Mapping", "Precise Shooting", "Riding", "Running", "Seafaring", "Skirmishing", "Skulking", "Sniping", "Swashbuckling", "Trap Finding", "Weapon Finesse", "Weapon Focus"]
	if cclass=="craftpriest":
		profs=["Alchemy", "Art", "Battle Magic", "Caving", "Collegiate Wizardry", "Contemplation", "Craft", "Diplomacy", "Divine Blessing", "Divine Health", "Dwarven Brewing", "Endurance", "Engineering", "Fighting Style", "Goblin-Slaying", "Healing", "Illusion Resistance", "Knowledge", "Laying on Hands", "Loremastery", "Magical Engineering", "Mapping", "Performance (chanting)", "Prestidigitation", "Profession (judge)", "Prophecy", "Quiet Magic", "Righteous Turning", "Sensing Evil", "Siege Engineering", "Theology", "Unflappable Casting", "Weapon Focus"]
	if cclass=="vaultguard":
		profs=["Alertness", "Berserkergang", "Blind Fighting", "Caving", "Combat Reflexes", "Combat Trickery (force back)", "Combat Trickery (knock down)", "Combat Trickery (overrun)", "Combat Trickery (sunder)", "Combat Trickery (wrestle)", "Command", "Craft", "Dungeon Bashing", "Dwarven Brewing", "Endurance", "Engineering", "Fighting Style", "Gambling", "Goblin-Slaying", "Illusion Resistance", "Intimidation", "Land Surveying", "Leadership", "Mapping", "Manual of Arms", "Military Strategy", "Mountaineering", "Siege Engineering", "Weapon Focus"]
	if cclass=="nightblade":
		profs=["Alchemy", "Alertness", "Battle Magic", "Beast Friendship", "Black Lore of Zahar", "Blind Fighting", "Combat Reflexes", "Combat Trickery (disarm)", "Combat Trickery (incapacitate)", "Contortionism", "Elementalism", "Familiar", "Fighting Style", "Intimidation", "Magical Engineering", "Mystic Aura", "Passing Without Trace", "Precise Shooting", "Prestidigitation", "Quiet Magic", "Running", "Sensing Power", "Skirmishing", "Skulking", "Sniping", "Swashbuckling", "Unflappable Casting", "Trap Finding", "Wakefulness", "Weapon Focus", "Weapon Finesse"]
	if cclass=="spellsword":
		profs=["Acrobatics", "Alertness", "Battle Magic", "Beast Friendship", "Black Lore of Zahar", "Blind Fighting", "Combat Reflexes", "Combat Trickery (disarm)", "Combat Trickery (knock down)", "Command", "Elementalism", "Familiar", "Fighting Style", "Leadership", "Loremastery", "Magical Engineering", "Magical Music", "Mystic Aura", "Naturalism", "Passing Without Trace", "Quiet Magic", "Precise Shooting", "Prestidigitation", "Running", "Sensing Power", "Skirmishing", "Soothsaying", "Swashbuckler", "Unflappable Casting", "Wakefulness", "Weapon Focus", "Weapon Finesse"]
	if level in [1,2] and cclass in ["assassin", "vaultguard", "spellsword", "explorer", "fighter"]:
		proflist.append(stellagama.random_choice(profs))
	elif level in [1, 2, 3] and cclass not in ["assassin", "vaultguard", "spellsword", "explorer", "fighter"]:
		proflist.append(stellagama.random_choice(profs))
	if level in [3, 4] and cclass in ["assassin", "vaultguard", "spellsword", "explorer", "fighter"]:
		for i in range (0,2):
			proflist.append(stellagama.random_choice(profs))
	elif level==4 and cclass not in ["assassin", "vaultguard", "spellsword", "explorer", "fighter"]:
		for i in range (0,2):
			proflist.append(stellagama.random_choice(profs))
	proficiencies=", ".join(proflist)
	return proficiencies #returns a list of class proficiencies
	
def profgen(intmod, level, cclass): #input character's intelligence modifier, level, and character class
	"""
	generate proficiency list
	"""
	proflist=genprofgen(level, intmod)
	proflist.append(classprof(level, cclass))
	return proflist #output proficiency list

def hp_gen(cclass, conmod, level): #input character class, constitution modifier, and level
	"""
	hit point generator
	"""
	if level==0:
		hp=stellagama.dice(1, 6)+conmod
	else:
		if cclass in ["fighter", "vaultguard"]:
			hp=stellagama.dice(level, 8)+conmod
		elif cclass in ["mage", "thief"]:
			hp=stellagama.dice(level, 4)+conmod
		elif cclass in ["assassin", "cleric", "bard", "bladedancer", "explorer", "craftpriest", "spellsword", "nightblade"]:
			hp=stellagama.dice(level, 6)+conmod
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
		return stellagama.random_choice(["Battle Axe", "Great Axe", "Hand Axe","Arbalest", "Crossbow", "Composite Bow", "Longbow", "Shortbow", "Club", "Flail", "Mace", "Morning Star", "Warhammer", "Javelin", "Pole Arm", "Spear", "Dagger", "Short Sword", "Sword", "Two-Handed Sword", "Staff", "Whip"])
	if cclass=="mage":
		return stellagama.random_choice(["Staff", "Club", "Dagger", "Dart"])
	if cclass=="cleric":
		return stellagama.random_choice(["Warhammer", "Mace", "Club", "Morning Star", "Staff", "Sling"])
	if cclass in ["thief", "bard", "explorer", "nightblade"]:
		return stellagama.random_choice(["Battle Axe", "Hand Axe", "Arbalest", "Crossbow", "Composite Bow", "Longbow", "Shortbow", "Club", "Flail", "Sap", "Mace", "Warhammer", "Javelin", "Spear", "Dagger", "Short Sword", "Sword", "Whip"])
	if cclass=="assassin":
		return stellagama.random_choice(["Hand Axe", "Hand Axe", "Arbalest", "Crossbow", "Crossbow", "Composite Bow", "Longbow", "Shortbow", "Dagger", "Dagger", "Dagger", "Dagger", "Dagger", "Short Sword", "Short Sword", "Short Sword", "Sword"])
	if cclass=="bladedancer":
		return stellagama.random_choice(["Battle Axe", "Great Axe", "Hand Axe", "Dagger", "Sword", "Sword", "Sword", "Shortsword", "Shortsword", "Two-Handed Sword", "Two-Handed Sword"])
	if cclass=="vaultguard":
		return stellagama.random_choice(["Battle Axe", "Battle Axe", "Battle Axe", "Great Axe", "Great Axe", "Great Axe", "Hand Axe", "Hand Axe", "Hand Axe", "Hand Axe", "Arbalest", "Crossbow", "Composite Bow", "Shortbow", "Club", "Flail", "Mace", "Warhammer", "Warhammer", "Warhammer", "Javelin", "Spear", "Dagger", "Short Sword", "Short Sword", "Whip"])
	if cclass=="craftpriest":
		return stellagama.random_choice(["Battle Axe", "Great Axe", "Hand Axe", "Flail", "Mace", "Morning Star", "Warhammer"])
	else:
		return stellagama.random_choice(["Staff", "Staff", "Staff", "Staff", "Club", "Club", "Club", "Club", "Dagger", "Dagger", "Dart", "Pitchfork", "Pitchfork", "Pitchfork", "Meat Cleaver", "Crowbar", "A Really Heavy Bell"])

def armor_gen (cclass): #input character class
	"""
	armor generation
	"""
	if cclass in ["fighter", "spellsword", "cleric", "vaultguard", "craftpriest"]:
		return stellagama.random_choice(["Leather Armor", "Scale Mail", "Scale Mail", "Chain Mail", "Chain Mail", "Chain Mail", "Banded Plate"])
	if cclass in ["thief", "bard", "assassin", "bladedancer", "nightblade"]:
		return stellagama.random_choice(["Clothes", "Clothes", "Hide Armor", "Leather Armor" ])
	if cclass == "explorer":
		return stellagama.random_choice (["clothes", "Hide Armor", "Leather Armor", "Scale Mail", "Chain Mail"])
	if cclass == "mage":
		return "Robes"
	else:
		return "Clothes"
