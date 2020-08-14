from tkinter import *
from tkinter import filedialog
from commands import *

class Bindings:
    def __init__(self, root, commands):
        self.root = root
        self.commands = commands
    
    def update(self):
        self.root.bind('<Control-n>', self.commands.new_file)
        self.root.bind('<Control-o>', self.commands.open_file)
        self.root.bind('<Control-s>', self.commands.save_file)
        self.root.bind('<Alt-s>', self.commands.save_file_as)
        self.root.bind('<Control-q>', self.commands.exit)
        self.root.bind('<Control-x>', self.commands.cut_text)
        self.root.bind('<Control-c>', self.commands.copy_text)
        self.root.bind('<Control-v>', self.commands.paste_text)