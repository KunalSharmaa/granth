from tkinter import *
from tkinter import filedialog
from commands import *

class Menus:
    def __init__(self, root, frame, text_box, status_bar, main_menu, commands):
        self.root = root
        self.frame = frame
        self.text_box = text_box
        self.status_bar = status_bar
        self.main_menu = main_menu
        self.commands = commands
        
    def create_file_menu(self):
        file_menu = Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label = "File", menu = file_menu)
        file_menu.add_command(label = "New      (Ctrl+n)", command = lambda: self.commands.new_file(False))
        file_menu.add_command(label = "Open     (Ctrl+o)", command = lambda: self.commands.open_file(False))
        file_menu.add_command(label = "Save     (Ctrl+s)", command = lambda: self.commands.save_file(False))
        file_menu.add_command(label = "Save As  (Alt+s)", command = lambda: self.commands.save_file_as(False))
        file_menu.add_separator()
        file_menu.add_command(label = "Exit     (Ctrl+q)", command = lambda: self.commands.exit(False))

    def create_edit_menu(self):
        edit_menu = Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label = "Edit", menu = edit_menu)
        edit_menu.add_command(label = "Cut      (Ctrl+x)", command = lambda: self.commands.cut_text(False))
        edit_menu.add_command(label = "Copy     (Ctrl+c)", command = lambda: self.commands.copy_text(False))
        edit_menu.add_command(label = "Paste    (Ctrl+v)", command = lambda: self.commands.paste_text(False))
        edit_menu.add_command(label = "Undo     (Ctrl+z)", command = self.text_box.edit_undo)
        edit_menu.add_command(label = "Redo     (Ctrl+y)", command = self.text_box.edit_redo)

    def create_tools_menu(self):
        tools_menu = Menu(self.main_menu, tearoff = False)
        highlight = Menu(tools_menu, tearoff = False)
        self.main_menu.add_cascade(label = "Tools", menu = tools_menu)
        tools_menu.add_cascade(label = "Highlight", menu = highlight)
        highlight.add_command(label = "Add Highlight", command = self.commands.add_highlight)
        highlight.add_command(label = "Remove Highlight", command = self.commands.remove_highlight)
        tools_menu.add_command(label = "Run Python Script", command = self.commands.run_script)
        tools_menu.add_command(label = "Find Text", command = self.commands.find_text)