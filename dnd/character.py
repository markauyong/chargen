#! python3

from util.dice import *
from dnd.races import *
from dnd.classes import *
from dnd.alignments import *
from dnd.skills import *
import math

class Character():
    @property
    def strength(self):
        return self.ability_score('str')
    @property
    def dexterity(self):
        return self.ability_score('dex')
    @property
    def constitution(self):
        return self.ability_score('con')
    @property
    def intelligence(self):
        return self.ability_score('int')
    @property
    def wisdom(self):
        return self.ability_score('wis')
    @property
    def charisma(self):
        return self.ability_score('cha')

    @property
    def passive_wisdom(self):
        return 10 + self.skill_bonus(11)

#-------------------------------------------------------------------------------
    def __init__(self):
        self.name = ""
        self.race = None
        self.cls = None
        self.lvl = 0
        self.base_ability = {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0 }
        self.race_mod = {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0 }
        self.skills = []
        self.hp = 0
        self.ac = 0
        self.speed = 0
        self.size = None
        self.darkVision = 0
        self.alignment = 0

        for i in range(0, len(skills)):
            self.skills.append(0)

#-------------------------------------------------------------------------------
    def generate_random(self):
        self.lvl = 1
        self.generate_random_abilities()
        self._generate_random_race()
        self._generate_random_class()
        self._generate_random_alignment()

#-------------------------------------------------------------------------------
    def generate_random_abilities(self):
        for i, v in enumerate(self.base_ability):
            self.base_ability[v] = roll_ability()

#-------------------------------------------------------------------------------
    def use_standard_abilities(self):
        self.base_ability['str'] = 15
        self.base_ability['dex'] = 14
        self.base_ability['con'] = 13
        self.base_ability['int'] = 12
        self.base_ability['wis'] = 10
        self.base_ability['cha'] = 8

#-------------------------------------------------------------------------------
    def _generate_random_race(self):
        self.race = randint(0, len(races) - 1)
        self.set_race()

#-------------------------------------------------------------------------------
    def _generate_random_class(self):
        self.cls = randint(0, len(classes) - 1)
        self.set_hp_for_level(self.lvl)

#-------------------------------------------------------------------------------
    def _generate_random_alignment(self):
        self.alignment = randint(0, len(alignments) - 1)

#-------------------------------------------------------------------------------
    def set_race(self):
        for i, v in enumerate(self.base_ability):
            self.race_mod[v] = self.racial_modifier_for_ability(v)
        self.speed = races[self.race]["speed"]
        if "darkVision" in races[self.race]:
            self.darkVision = races[self.race]["darkVision"]
        else:
            self.darkVision = 0

#-------------------------------------------------------------------------------
    def set_hp_for_level(self, level):
        self.hp = 0
        for i in range(0, level):
            if i == 0:
                self.hp += classes[self.cls]["hitDie"] + ability_modifier(self.constitution)
            else:
                self.hp += classes[self.cls]["fixedHP"] + ability_modifier(self.constitution)

#-------------------------------------------------------------------------------
    def ability_score(self, ability):
        return self.base_ability[ability] + self.race_mod[ability]

#-------------------------------------------------------------------------------
    def racial_modifier_for_ability(self, ability):
        raceMod = 0
        if ability in races[self.race]['abilityModifier']:
            raceMod = races[self.race]['abilityModifier'][ability]
        return raceMod

#-------------------------------------------------------------------------------
    def skill_bonus(self, skill):
        bonus = ability_modifier(self.ability_score(skills[skill]["ability"]))
        if (self.skills[skill] == 1):
            bonus = bonus + proficiency_bonus(self.lvl)
        return bonus

#-------------------------------------------------------------------------------
    def skills_selected(self):
        selected = 0
        for i in self.skills:
            selected = selected + i

        return selected

#-------------------------------------------------------------------------------
    def all_skills_selected(self):
        return self.skills_selected() == classes[self.cls]["numSkills"]

#-------------------------------------------------------------------------------
    def reset_skills(self):
        for i in range(0, len(self.skills)):
            self.skills[i] = 0

#-------------------------------------------------------------------------------
    def saving_throw(self, ability):
        class_specific = False
        saving_throw = ability_modifier(self.ability_score(ability))
        if ability in classes[self.cls]['savingThrows']:
            saving_throw += proficiency_bonus(self.lvl)
            class_specific = True

        return saving_throw, class_specific

#-------------------------------------------------------------------------------
def ability_modifier(ability):
    modifier = math.floor(ability / 2.0) - 5
    return modifier

#-------------------------------------------------------------------------------
def proficiency_bonus(level):
    bonus = math.floor((level - 1) / 4.0) + 2
    return bonus

#-------------------------------------------------------------------------------
def roll_ability():
    rolls = d6.roll_list(4)
    rolls.sort(reverse = True)
    result = rolls[0] + rolls[1] + rolls[2]
    #print("{} {}".format(rolls, result))
    return result
