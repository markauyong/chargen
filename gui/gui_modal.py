#! python 3

import sys
sys.path.append('../')

from tkinter import *
from tkinter.ttk import *

class ModalWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_form()
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.withdraw()

    def create_form(self):
        #self.minsize(300, 100)
        self.content_frame = Frame(self)
        self.content_frame.grid(row=0)
        self.button_frame = Frame(self)
        self.button_frame.grid(row=1)

        self.btn_done = Button(self.button_frame, text="Done", command=self.close)
        self.btn_done.grid(row=0, column=0, padx=5)

    def show(self):
        #self.wm_attributes("-topmost", True)
        self.parent.attributes("-alpha", 0.90)
        self.deiconify()
        self.lift()
        self.grab_set()

    def close(self):
        self.grab_release()
        self.withdraw()
        self.parent.attributes("-alpha", 1.0)
        self.parent.lift()
        #self.destroy()
