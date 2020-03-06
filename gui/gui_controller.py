#! python 3

import sys
sys.path.append('../')

from dnd.character import *
from dnd.classes import *
from gui.gui_form import *

class Controller():

    def __init__(self, form):
        self.character = None
        self.form = form

        for i in range(0, len(self.form.skill)):
            self.form.skill[i].bind_click(self.update_skills)

        # Half-Elf special case allows player to specify one ability (except charisma)
        # to give a +1 racial bonus. Bind the racial bonus entry box for these abilities
        # to left button click so the user can choose an ability.
        for i in range(0, len(self.form.asf_ability) - 1):
            self.form.asf_ability[i].bind_click(self.pick_half_elf_ability)

        # Blue font style as a visual indicator for player to select an ability when
        # creating a Half-Elf
        style = Style()
        style.configure('RB.TEntry', foreground='blue')
        style.configure('RB.TLabel', foreground='blue')

        self.form.m_hint.config(style="RB.TLabel")

#-------------------------------------------------------------------------------
    def update_skills(self, event, idx):
        if str(event.widget['state']) == 'normal':
            if event.widget.value.get() == False:
                if self.character.all_skills_selected():
                    # Set the checkbox to selected so that that the tk.Checkbutton toggle will change it back to deselected
                    event.widget.value.set(True)
                else:
                    self.character.skills[idx] = 1
            else:
                if self.character.skills[idx] == 1:
                    self.character.skills[idx] = 0

        self.display_character()

#-------------------------------------------------------------------------------
    def assign_character(self, character):
        self.reset_skills()
        self.character = character
        self.set_skill_boxes()

#-------------------------------------------------------------------------------
    def entry_box_updated(self, eb):
        self.character.name = eb.get()

#-------------------------------------------------------------------------------
    def display_character(self):
        self.check_for_half_elf()

        self.form.e_name.set(self.character.name)
        self.form.cb_class.current(self.character.cls)
        self.form.cb_level.current(self.character.lvl - 1)
        self.form.cb_race.current(self.character.race)
        self.form.cb_alignment.current(self.character.alignment)

        #form.e_str.delete(0,END)
        #form.e_str.insert(0,self.character.strength)

        for i, v in enumerate(['str', 'dex', 'con', 'int', 'wis', 'cha']):
            self.form.asf_ability[i].set_base(self.character.base_ability[v])
            self.form.asf_ability[i].set_race_mod(self.character.race_mod[v])
            self.form.asf_ability[i].set_ability(self.character.ability_score(v))
            self.form.asf_ability[i].set_bonus("{0:+0d}".format(ability_modifier(self.character.ability_score(v))))

        for i, v in enumerate(['str', 'dex', 'con', 'int', 'wis', 'cha']):
            savingThrow, classSpecific = self.character.saving_throw(v)
            self.form.saving_throw[i].set_value("{0:+0d}".format(savingThrow))
            if classSpecific:
                self.form.saving_throw[i].tick()
            else:
                self.form.saving_throw[i].untick()

        for i in range(0, len(skills)):
            self.form.skill[i].set_value("{0:+0d}".format(self.character.skill_bonus(i)))
            if "skillChoices" in classes[self.character.cls] and \
                (i in classes[self.character.cls]["skillChoices"] or classes[self.character.cls]["skillChoices"][0] == 'all'):
                self.form.skill[i].enable()
            else:
                self.form.skill[i].disable()

        self.form.l_skill_info['text'] = 'Skills selected: ' + str(self.character.skills_selected()) + '/' + str(classes[self.character.cls]['numSkills'])

        self.form.ebf_hp.set_value(self.character.hp)
        self.form.ebf_prof_bonus.set_value("{0:+0d}".format(proficiency_bonus(self.character.lvl)))
        self.form.ebf_speed.set_value(races[self.character.race]["speed"])
        if "darkVision" in races[self.character.race]:
            self.form.ebf_darkvision.set_value(races[self.character.race]["darkVision"])
        else:
            self.form.ebf_darkvision.set_value("N/A")
        self.form.ebf_passive_wis.set_value(self.character.passive_wisdom)

#-------------------------------------------------------------------------------
    def check_for_half_elf(self):
        for i, v in enumerate(['str', 'dex', 'con', 'int', 'wis']):
            if races[self.character.race]["race"] == "Half-Elf":
                self.form.asf_ability[i].set_style("RB.TEntry")
                self.form.m_hint["text"] = "Click racial box to set bonus"
            else:
                self.form.asf_ability[i].set_style("TEntry")
                self.form.m_hint["text"] = ""

#-------------------------------------------------------------------------------
    def pick_half_elf_ability(self, event, idx):
        if races[self.character.race]["race"] == "Half-Elf":
            for i, v in enumerate(['str', 'dex', 'con', 'int', 'wis']):
                if i == idx:
                    self.character.race_mod[v] = 1
                else:
                    self.character.race_mod[v] = 0

        self.display_character()

#-------------------------------------------------------------------------------
    def arrange_abilities(self, new_arrangement):
        for i, v in enumerate(self.character.base_ability):
            self.character.base_ability[v] = int(new_arrangement[i])
        self.character.set_hp_for_level(self.character.lvl)
        self.display_character()

#-------------------------------------------------------------------------------
    def reroll_abilities(self):
        self.character.generate_random_abilities()
        self.display_character()

#-------------------------------------------------------------------------------
    def use_standard_abilities(self):
        self.character.use_standard_abilities()
        self.display_character()

#-------------------------------------------------------------------------------
    def race_change(self, event):
        self.character.race = self.form.cb_race.current()
        self.character.set_race()
        self.display_character()

#-------------------------------------------------------------------------------
    def class_change(self, event):
        self.character.cls = self.form.cb_class.current()
        self.character.set_hp_for_level(self.character.lvl)
        self.reset_skills()
        self.display_character()

#-------------------------------------------------------------------------------
    def level_change(self, event):
        self.character.lvl = self.form.cb_level.current() + 1
        self.character.set_hp_for_level(self.character.lvl)
        self.display_character()

#-------------------------------------------------------------------------------
    def alignment_change(self, event):
        self.character.alignment = self.form.cb_alignment.current()
        self.display_character()

#-------------------------------------------------------------------------------
    def set_skill_boxes(self):
        if self.character is not None:
            for i, v in enumerate(self.form.skill):
                if self.character.skills[i]:
                    self.form.skill[i].tick()
                else:
                    self.form.skill[i].untick()

#-------------------------------------------------------------------------------
    def reset_skills(self):
        if self.character is not None:
            self.character.reset_skills()
        for i in self.form.skill:
            i.untick()
