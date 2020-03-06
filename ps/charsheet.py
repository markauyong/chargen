#! python3

import sys
sys.path.append('../')

from dnd.character import *
from dnd.races import *
from dnd.classes import *
from dnd.alignments import *
from dnd.skills import *

class PSChar():

    _bullet_func = "/bullet { 3 0 360 arc closepath fill } def "

    _header = "gsave initmatrix "
    _footer = "grestore showpage %%EOF"

    size_name = 18
    pos_name = (45, 705)

    size_info = 11
    pos_class = (262, 719)
    pos_race = (262, 693)
    pos_alignment = (374, 693.5)

    size_prof_bonus = 18
    pos_prof_bonus = (90, 598)

    size_speed = 24
    pos_speed = (342.5, 615)

    size_passive_wis = 14
    pos_passive_wis_x_single = 31
    pos_passive_wis_x_double = 27
    pos_passive_wis_y = 178.5

    size_ability = 24
    pos_ability_x_single = 43
    pos_ability_x_double = 36
    pos_ability_y_start = 605
    pos_ability_y_offset = 71.5

    size_ability_mod = 12
    pos_ability_mod = (42, 585)
    pos_ability_mod_y_offset = 71.8

    size_hp = 12
    pos_hp = (300, 575)

    pos_save = (95.8, 570)
    pos_save_y_offset = 13.5
    size_save_text = 10
    pos_save_text = (106, 568)
    pos_save_text_y_offset = 13.5

    pos_skills = (96, 455)
    pos_skills_y_offset = 13.5
    size_skills_text = 10
    pos_skills_text = (106, 453)
    pos_skills_text_y_offset = 13.5

    size_darkvision = 10
    pos_darkvision = (404, 378)

#-------------------------------------------------------------------------------
    def printChar(self, char, filename):
        with open(filename, 'w') as outfile:
            with open('sheet_template.ps') as infile:
                for line in infile:
                    outfile.write(line)

            outfile.write(PSChar._header)
            outfile.write(PSChar._bullet_func)

            self._print_single_items(char, outfile)
            self._print_abilities_and_saving_throws(char, outfile)
            self._print_skills(char, outfile)

            outfile.write(PSChar._footer)

#-------------------------------------------------------------------------------
    def _set_font_size(self, size):
        return "/Times-Roman findfont {} scalefont setfont ".format(size)

#-------------------------------------------------------------------------------
    def _print_text(self, text, font_size, pos):
        ret_string = self._set_font_size(font_size)
        ret_string = ret_string + "{} {} moveto ".format(pos[0], pos[1])
        ret_string = ret_string + "({}) show ".format(text)
        return ret_string

#-------------------------------------------------------------------------------
    def _print_single_items(self, char, outfile):
            if char.name is not None:
                outfile.write(self._print_text(char.name, PSChar.size_name, PSChar.pos_name))

            outfile.write(self._print_text(
                classes[char.cls]["class"] + " " + str(char.lvl),
                PSChar.size_info,
                PSChar.pos_class))

            outfile.write(self._print_text(
                full_race_name(char.race),
                PSChar.size_info,
                PSChar.pos_race))

            outfile.write(self._print_text(
                alignments[char.alignment]["alignment"],
                PSChar.size_info,
                PSChar.pos_alignment))

            outfile.write(self._print_text(
                char.hp,
                PSChar.size_hp,
                PSChar.pos_hp))

            outfile.write(self._print_text(
                "{0:+0d}".format(proficiency_bonus(char.lvl)),
                PSChar.size_prof_bonus,
                PSChar.pos_prof_bonus))

            outfile.write(self._print_text(
                char.speed,
                PSChar.size_speed,
                PSChar.pos_speed))

            x = PSChar.pos_passive_wis_x_double
            if char.passive_wisdom < 10:
                x = PSChar.pos_passive_wis_x_single
            y = PSChar.pos_passive_wis_y
            pos = (x, y)

            outfile.write(self._print_text(
                char.passive_wisdom,
                PSChar.size_passive_wis,
                pos))

            if char.darkVision > 0:
                outfile.write(self._print_text(
                    "Darkvision: {}".format(char.darkVision),
                    PSChar.size_darkvision,
                    PSChar.pos_darkvision))

#-------------------------------------------------------------------------------
    def _print_abilities_and_saving_throws(self, char, outfile):
        for i, v in enumerate(['str', 'dex', 'con', 'int', 'wis', 'cha']):
            ability = char.ability_score(v)
            x = PSChar.pos_ability_x_double
            if ability < 10:
                x = PSChar.pos_ability_x_single
            y = PSChar.pos_ability_y_start - (PSChar.pos_ability_y_offset * i)
            pos = (x, y)

            outfile.write(self._print_text(
                char.ability_score(v),
                PSChar.size_ability,
                pos))

            mod = ability_modifier(ability)
            x = PSChar.pos_ability_mod[0]
            y = PSChar.pos_ability_mod[1] - (PSChar.pos_ability_mod_y_offset * i)
            pos = (x, y)

            outfile.write(self._print_text(
                "{0:+0d}".format(mod),
                PSChar.size_ability_mod,
                pos))

            save_throw, class_specific = char.saving_throw(v)
            if class_specific:
                x = PSChar.pos_save[0]
                y = PSChar.pos_save[1] - (PSChar.pos_save_y_offset * i)
                outfile.write("newpath {} {} bullet ".format(x, y))

            x = PSChar.pos_save_text[0]
            y = PSChar.pos_save_text[1] - (PSChar.pos_save_text_y_offset * i)
            pos = (x, y)

            outfile.write(self._print_text(
                "{0:+0d}".format(save_throw),
                PSChar.size_save_text,
                pos))

#-------------------------------------------------------------------------------
    def _print_skills(self, char, outfile):
        for i in range(0, len(skills)):
            bonus = char.skill_bonus(i)
            x = PSChar.pos_skills_text[0]
            y = PSChar.pos_skills_text[1] - (PSChar.pos_skills_text_y_offset * i)
            pos = (x, y)

            outfile.write(self._print_text(
                "{0:+0d}".format(bonus),
                PSChar.size_skills_text,
                pos))

            if char.skills[i] == 1:
                x = PSChar.pos_skills[0]
                y = PSChar.pos_skills[1] - (PSChar.pos_skills_y_offset * i)
                outfile.write("newpath {} {} bullet ".format(x, y))
