#! python3

from util.dice import *
from util.file_handler import *

from dnd.races import *
from dnd.classes import *
from dnd.character import *

from gui.gui_form import *
from gui.gui_controller import *
from gui.gui_modal_ability_select import *

from ps.charsheet import *

from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *

import math
import os

class MenuBar(Menu):
    def __init__(self, parent):
        super().__init__(parent)

        self._filemenu = Menu(self, tearoff=0)
        self._filemenu.add_command(label="Roll Character", command=generate_random_char)
        self._filemenu.add_separator()
        self._filemenu.add_command(label="Save", command=save_file)
        self._filemenu.add_command(label="Load", command=load_file)
        self._filemenu.add_separator()
        self._filemenu.add_command(label="Save Sheet", command=create_sheet)
        self._filemenu.add_separator()
        self._filemenu.add_command(label="Quit", command=self.master.quit)
        
        self.add_cascade(label="File", menu=self._filemenu)

        parent.config(menu=self)

#-------------------------------------------------------------------------------
def generate_random_char():
    random_char = Character()
    random_char.generate_random()
    ctl.assign_character(random_char)
    ctl.display_character()

#-------------------------------------------------------------------------------
def create_sheet():
    if not os.path.isdir("saves"):
        os.mkdir("saves")
        
    savefile = filedialog.asksaveasfilename(initialdir = "./saves", filetypes = (("postscript files","*.ps"),("all files","*.*")))
    
    if savefile != "":
        if savefile[-3:] != ".ps":
            savefile = savefile + ".ps"
        pt = PSChar()
        pt.printChar(ctl.character, savefile)

#-------------------------------------------------------------------------------
def save_file():
    if not os.path.isdir("saves"):
        os.mkdir("saves")

    savefile = filedialog.asksaveasfilename(initialdir = "./saves", filetypes = (("character files","*.chr"),("all files","*.*")))

    if savefile != "":
        if savefile[-4:] != ".chr":
            savefile = savefile + ".chr"

        save_to_file(savefile, ctl.character)

#-------------------------------------------------------------------------------
def load_file():
    startdir = "./saves"
    if not os.path.isdir("saves"):
        startdir = "./"

    loadfile = filedialog.askopenfilename(initialdir = startdir, filetypes = (("character files","*.chr"),("all files","*.*")))

    if os.path.isfile(loadfile):
        loadedChar = load_from_file(loadfile)
        ctl.assign_character(loadedChar)
        ctl.display_character()

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

root = Tk()
root.title("chargen")

menubar = MenuBar(root)
form = CharacterForm(root)
separator = Separator(root, orient="horizontal")
separator.pack(anchor="nw", fill=X)
buttonBar = ButtonBar(root, 3)

ctl = Controller(form)
generate_random_char()
form.set_controller(ctl)

ability_modal = AbilityModalWindow(root, controller=ctl)

buttonBar.assign_button(0, "Arrange Abilities", ability_modal.show)
buttonBar.assign_button(1, "Re-roll Abilities", ctl.reroll_abilities)
buttonBar.assign_button(2, "Use Fixed Ability Scores", ctl.use_standard_abilities)

c = ctl.character

#print(root.wm_attributes())

form.mainloop()
#root.destroy()
