#! python 3

import sys
sys.path.append('../')


from tkinter import *
from gui.gui_modal import *
from gui.gui_widgets import *
from functools import partial

class AbilityModalWindow(ModalWindow):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller
        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.current_selection = None
        self.e_ability = []
        self.btn_ability = []

        self.configure(padx=10, pady=10)

        self.title("Arrange Abilities")
        self.create_ability_form()

#-------------------------------------------------------------------------------
    def create_ability_form(self):
        self.btn_done["text"] = "Accept"
        self.btn_cancel = Button(self.button_frame, text="Cancel", command=self.cancel)
        self.btn_cancel.grid(row=0, column=1, padx=10)

        self.ability_frame = Frame(self.content_frame)
        self.ability_frame.grid(row=0, column=0)
        self.info_frame = Frame(self.content_frame)
        self.info_frame.grid(row=1, column=0)

        for i in range(6):
            button_pressed = partial(self.switch_abilities, i)

            self.btn_ability.append(Button(self.ability_frame, width=5, command=button_pressed))
            self.btn_ability[i].grid(row=i, column=0, pady=2)

            self.e_ability.append(EntryBox(self.ability_frame, width=3))
            self.e_ability[i].grid(row=i, column=1, padx=(8,0))

        self.info_textbox = Message(self.info_frame, width=300, relief=FLAT, pady=10)
        self.info_textbox.pack()
        self.info_textbox["text"] = "Click two ability buttons to switch abilties"

#-------------------------------------------------------------------------------
    def set_abilities(self, ability_list):
        for i, v in enumerate(ability_list):
            self.btn_ability[i]["text"] = v
            self.e_ability[i].set(ability_list[v])

#-------------------------------------------------------------------------------
    def switch_abilities(self, selected):
        if self.current_selection is None:
            self.current_selection = selected
            self.e_ability[selected].configure(foreground = 'red')
        else:
            if self.current_selection != selected:
                self.tmp_ability = self.e_ability[self.current_selection].get()
                self.e_ability[self.current_selection].set(self.e_ability[selected].get())
                self.e_ability[selected].set(self.tmp_ability)

            self.e_ability[self.current_selection].configure(foreground = 'black')
            self.current_selection = None

#-------------------------------------------------------------------------------
    def show(self):
        super().show()
        self.set_abilities(self.controller.character.base_ability)

#-------------------------------------------------------------------------------
    def close(self):
        new_arrangement = []
        for i in range(len(self.e_ability)):
            new_arrangement.append(self.e_ability[i].get())
        self.controller.arrange_abilities(new_arrangement)
        super().close()

#-------------------------------------------------------------------------------
    def cancel(self):
        super().close()
