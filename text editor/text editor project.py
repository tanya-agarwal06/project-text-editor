import os
import tkinter
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import *


class texteditor:
    def __init__(self, root):
        self.file_path = None
        self.menu = Menu(root)
        root.config(self.menu)
        self.Submenu = Menu(self.menu)
        Menu = self.menu.add_cascade(label="File", menu = self.Submenu)
        self.Submenu.add_command(label="New File" , command= self.t_1)

    def t_1(self):
        print("text edit")
root = Tk()
a = texteditor(root)


root.mainloop()
