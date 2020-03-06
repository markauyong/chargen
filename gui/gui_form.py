#! python 3

import sys
sys.path.append('../')

from tkinter import *
from gui.gui_widgets import *
from dnd.races import *
from dnd.classes import *
from dnd.alignments import *
from dnd.skills import *

class CharacterForm(Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controller = None
        self.pack(padx=5, pady=(0, 10))

        self.create_grid()

#-------------------------------------------------------------------------------
    def set_controller(self, controller):
        self.controller = controller
        self.e_name.set_controller(self.controller)
        self.cb_race.bind("<<ComboboxSelected>>", self.controller.race_change)
        self.cb_class.bind("<<ComboboxSelected>>", self.controller.class_change)
        self.cb_level.bind("<<ComboboxSelected>>", self.controller.level_change)
        self.cb_alignment.bind("<<ComboboxSelected>>", self.controller.alignment_change)

#-------------------------------------------------------------------------------
    def create_grid(self):

        self.create_info_frame()
        self.create_ability_save_frame()
        self.create_skill_frame()
        self.create_stats_frame()

#-------------------------------------------------------------------------------
    def create_info_frame(self):
        self.f_info = LabelFrame(self)
        self.f_info['text'] = 'Basic Info'
        self.f_info['padding'] = '10 10'
        self.f_info.grid(row=0, column=0, columnspan=3, sticky='w')

        # Name
        self.l_name = Label(self.f_info, text="CHARACTER NAME")
        self.l_name.grid(row=0, column=0, sticky="wn")
        self.e_name = EntryBox(self.f_info, width=37)
        self.e_name.enable()
        self.e_name.grid(row=1, column=0, rowspan=2, sticky="n")

        # Class
        self.l_class = Label(self.f_info, text="CLASS")
        self.l_class.grid(row=0, column=2, padx=10, sticky="wn")
        self.cb_class = ComboBox(self.f_info)
        self.cb_class["values"] = class_list()
        self.cb_class.grid(row=1, column=2, padx=10, pady=(0,5))

        # Level
        self.l_level = Label(self.f_info, text="LEVEL")
        self.l_level.grid(row=0, column=3, sticky="wn")
        self.cb_level = ComboBox(self.f_info)

        lvls = []
        for i in range(1, 31):
            lvls.append(i)

        self.cb_level["values"] = lvls
        self.cb_level.grid(row=1, column=3, pady=(0,5))

        # Race
        self.l_race = Label(self.f_info, text="RACE")
        self.l_race.grid(row=2, column=2, padx=10, sticky="wn")
        self.cb_race = ComboBox(self.f_info)
        self.cb_race["values"] = race_list()
        self.cb_race.grid(row=3, column=2)

        # Alignment
        self.l_alignment = Label(self.f_info, text="ALIGNMENT")
        self.l_alignment.grid(row=2, column=3, sticky="wn")
        self.cb_alignment = ComboBox(self.f_info)
        self.cb_alignment["values"] = alignment_list()
        self.cb_alignment.grid(row=3, column=3)

#-------------------------------------------------------------------------------
    def create_ability_save_frame(self):
        self.f_abl_save = Frame(self)
        self.f_abl_save.grid(row=1, column=0, rowspan=2, sticky='nw', pady=(5, 0), padx=5)
        self.create_ability_frame(self.f_abl_save)
        self.create_saving_throw_frame(self.f_abl_save)

#-------------------------------------------------------------------------------
    def create_saving_throw_frame(self, parent):
        self.f_saving = LabelFrame(parent)
        self.f_saving['text'] = 'Saving Throws'
        self.f_saving['padding'] = '10 10'
        self.f_saving.grid(row = 2, column = 0, sticky="nw", pady=(5, 0))

        self.saving_throw = []

        for i, v in enumerate(['str', 'dex', 'con', 'int', 'wis', 'cha' ]):
            self.saving_throw.append(CheckBoxInfoFrame(self.f_saving, str.upper(v)))
            self.saving_throw[i].disable()
            self.saving_throw[i].grid(row=i, sticky="w")

#-------------------------------------------------------------------------------
    def create_ability_frame(self, parent):
        self.f_ability = LabelFrame(parent)
        self.f_ability['text'] = 'Abilities'
        self.f_ability['padding'] = '10 10'
        self.f_ability.grid(row=1, column=0, sticky="nw")

        self.asf_ability_headings = AbilityStatFrame(self.f_ability, text="")
        self.asf_ability_headings.grid(row=0, sticky="w")
        self.asf_ability_headings.set_base("DR")
        self.asf_ability_headings.set_race_mod("RB")
        self.asf_ability_headings.set_ability("AS")
        self.asf_ability_headings.set_bonus("AM")

        self.asf_ability = []
        for i, v in enumerate(['str', 'dex', 'con', 'int', 'wis', 'cha' ]):
            self.asf_ability.append(AbilityStatFrame(self.f_ability, text=str.upper(v), idx=i))
            self.asf_ability[i].grid(row=i + 1, sticky="w")

        self.m_ability_info = Message(self.f_ability, width=150)
        self.m_ability_info.grid(row=7, column=0, sticky="nw", pady=5)
        self.m_ability_info["text"] = "DR - Dice Roll\nRB - Racial Bonus\nAS - Ability Score\nAM - Ability Modifier"

        self.m_hint = Label(self.f_ability)
        self.m_hint.grid(row=8, column=0, pady=5)

#-------------------------------------------------------------------------------
    def create_skill_frame(self):
        self.f_skill = LabelFrame(self)
        self.f_skill['text'] = 'Skills'
        self.f_skill['padding'] = '10 10'
        self.f_skill.grid(row=1, column=1, pady=(5, 0))

        self.skill = []

        for i in range(0, len(skills)):
            self.skill.append(CheckBoxInfoFrame(self.f_skill, "{} ({})".format(skills[i]["skill"], skills[i]["ability"]) ))
            self.skill[i].grid(row=i, sticky="w")
            self.skill[i].set_index(i)

        self.l_skill_info = Label(self.f_skill)
        self.l_skill_info.grid(row=len(skills), pady=(5, 0), sticky="n")
        self.l_skill_info['text'] = ''

#-------------------------------------------------------------------------------
    def create_stats_frame(self):
        self.f_stats = LabelFrame(self)
        self.f_stats['text'] = 'Stats'
        self.f_stats['padding'] = '10 10'
        self.f_stats.grid(row=1, column=2, pady=(5, 0), padx=5, sticky="n")

        labelWidth=18
        row = 0
        self.ebf_hp = LabelEntryBoxFrame(self.f_stats, "HP", width=labelWidth)
        self.ebf_hp.grid(row=row, column=0, sticky=W)

        row = row + 1
        self.ebf_prof_bonus = LabelEntryBoxFrame(self.f_stats, "Proficiency Bonus", width=labelWidth)
        self.ebf_prof_bonus.grid(row=row, column=0, sticky=W, pady=(0, 10))

        row = row + 1
        self.ebf_speed = LabelEntryBoxFrame(self.f_stats, "Speed", width=labelWidth)
        self.ebf_speed.grid(row=row, column=0, sticky=W)

        row = row + 1
        self.ebf_darkvision = LabelEntryBoxFrame(self.f_stats, "Darkvision", width=labelWidth)
        self.ebf_darkvision.grid(row=row, column=0, sticky=W, pady=(0,10))

        row = row + 1
        self.ebf_passive_wis = LabelEntryBoxFrame(self.f_stats, "Passive Wisdom", width=labelWidth)
        self.ebf_passive_wis.grid(row=row, column=0, sticky=W)
