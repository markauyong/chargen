#! python 3

""" Several wrappers for standard tk widgets to combine with tk vars
    and some widgets grouped inside frames
"""

from tkinter import *
from tkinter.ttk import *

class EntryBox(Entry):
    def __init__(self, parent=None, controller=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.controller = controller

        self.contents = StringVar()
        self["textvariable"] = self.contents
        self.bind('<Key-Return>',
                  self.update_contents)
        self.bind('<Leave>',
                  self.update_contents)

        self.disable()

    def set(self, in_string):
        self.contents.set(in_string)

    def get(self):
        return self.contents.get()

    def enable(self):
        self.config(state='normal')

    def disable(self):
        self.config(state='readonly')

    def set_controller(self, controller):
        self.controller = controller

    def update_contents(self, event):
        if self.controller is not None:
            if self.master.focus_get() is self:
                self.controller.entry_box_updated(self)

#-------------------------------------------------------------------------------
class ComboBox(Combobox):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(state='readonly')

#-------------------------------------------------------------------------------
class CheckButton(Checkbutton):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.value = IntVar()
        self.configure(variable=self.value)

#-------------------------------------------------------------------------------
class AbilityStatFrame(Frame):
    def __init__(self, parent=None, text='Ability', idx=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.init_components(text, **kwargs)
        self.idx = idx

    def init_components(self, text, width=5, **kwargs):
        self.label = Label(self, text=text, width=width)
        self.label.grid(row=0, column=0)

        self.base_ability = EntryBox(self, width=4)
        self.base_ability.grid(row=0, column=1)

        self.race_mod = EntryBox(self, width=4)
        self.race_mod.grid(row=0, column=2)

        self.ability = EntryBox(self, width=4)
        self.ability.grid(row=0, column=3)

        self.ability_bonus = EntryBox(self, width=4)
        self.ability_bonus.grid(row=0, column=4)

    def set_base(self, base):
        self.base_ability.set(base)

    def set_race_mod(self, race_mod):
        self.race_mod.set(race_mod)

    def set_ability(self, ability):
        self.ability.set(ability)

    def set_bonus(self, bonus):
        self.ability_bonus.set(bonus)

    def bind_click(self, callback):
        self.race_mod.bind("<Button-1>", lambda event: callback(event, self.idx))

    def set_style(self, style):
        self.race_mod.configure(style=style)

#-------------------------------------------------------------------------------
class LabelEntryBoxFrame(Frame):
    def __init__(self, parent=None, text="Label", **kwargs):
        super().__init__(parent, **kwargs)
        self.init_components(text, **kwargs)
        self.idx = None

    def init_components(self, text, width=10, **kwargs):
        self.label = Label(self, text=text, width=width)
        self.label.grid(row=0, column=0)

        self.entryBox = EntryBox(self, width=4)
        self.entryBox.grid(row=0, column=1)

    def set_value(self, value):
        self.entryBox.set(value)

#-------------------------------------------------------------------------------
class CheckBoxInfoFrame(Frame):
    def __init__(self, parent=None, text="Default", **kwargs):
        super().__init__(parent, **kwargs)
        self.init_components(text)
        self.idx = None

    def init_components(self, text):
        self.checkBox = CheckButton(self)
        self.checkBox.grid(row=0, column=0)

        self.entryBox = EntryBox(self, width=4)
        self.entryBox.grid(row=0, column=1)

        self.label = Label(self, text=text)
        self.label.grid(row=0, column=2)

    def set_value(self, value):
        self.entryBox.set(value)

    def set_index(self, idx):
        self.idx = idx

    def disable(self):
        self.checkBox.config(state=DISABLED)

    def enable(self):
        self.checkBox.config(state=NORMAL)

    def tick(self):
        self.checkBox.value.set(True)

    def untick(self):
        self.checkBox.value.set(False)

    def bind_click(self, callback):
        self.checkBox.bind("<Button-1>", lambda event: callback(event, self.idx))

#-------------------------------------------------------------------------------
class ButtonBar(Frame):
    def __init__(self, parent=None, buttons=1, **kwargs):
        super().__init__(parent, **kwargs)

        self.button = []
        for i in range(0, buttons):
            self.button.append(Button(self, text="Click Me!", command=self._dummy_command))
            self.button[i].pack(side=LEFT, padx=2)

        self.pack(expand=1, pady=15)

    def _dummy_command(self):
        print("Button clicked")

    def assign_button(self, idx, text, command):
        self.button[idx].configure(text=text, command=command)
