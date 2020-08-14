from tkinter import *
from tkinter import filedialog
import os

global opened_text_file
opened_text_file = False

global selected_text
selected_text = False

class Commands:
    def __init__(self, root, frame, text_box, status_bar):
        self.root = root
        self.frame = frame
        self.text_box = text_box
        self.status_bar = status_bar

    #function to create new file
    def new_file(self, e):
        #delete any existing text
        self.text_box.delete(1.0, END)
        
        #update status bars
        self.root.title('New File - Granth')
        self.status_bar.config(text = "New File        ")
        
        global opened_text_file
        opened_text_file = False

    #function to Open existing files    
    def open_file(self, e):
        #delete any existing text
        self.text_box.delete(1.0, END)
        
        #grab filename
        global opened_text_file
        opened_text_file = filedialog.askopenfilename(initialdir = "D:/projects/", title = "Open File", filetypes = (("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py")))
        
        if opened_text_file:
            #update status bars
            filename = opened_text_file
            self.status_bar.config(text = f'{filename}        ')
            filename = os.path.basename(filename)
            self.root.title(f'{filename} - Granth')
            
            #open the file
            with open(opened_text_file, 'r') as fh:
                file_content = fh.read()
            
            #add file content to text box
            self.text_box.insert(END, file_content)
        else:
            pass

    #function to save overwritten files    
    def save_file(self, e):
        global opened_text_file
        if opened_text_file:
            with open(opened_text_file, 'w') as fh:
                fh.write(self.text_box.get(1.0, END))
            self.status_bar.config(text = f'Saved: {opened_text_file}')
        else:
            self.save_file_as(False)
        

    #function to save new files
    def save_file_as(self, e):
        text_file = filedialog.asksaveasfilename(defaultextension = ".*", initialdir = "D:/projects/", title = "Save File", filetypes = (("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py")))
        
        #check if file exists, since we have the option of cancel as well in the dialog box
        if text_file:
            #update status bars
            filename = text_file
            self.status_bar.config(text = f' Saved: {filename}        ')
            filename = os.path.basename(filename)
            self.root.title(f'{filename} - Granth')
            
            #save the file
            with open(text_file, 'w') as fh:
                fh.write(self.text_box.get(1.0, END))
            
            global opened_text_file
            opened_text_file = text_file
            
    def exit(self, e):
        self.root.quit()
            
    #function to perform cut text operation
    def cut_text(self, e):
        try:
            global selected_text
        
            #check to see if keyboard shortcut is used
            if e:
                selected_text = self.root.clipboard_get()
            
            else:
                if self.text_box.selection_get():
                    selected_text = self.text_box.selection_get()
                    self.text_box.delete("sel.first", "sel.last")
                    self.root.clipboard_clear()
                    self.root.clipboard_append(selected_text)
        except TclError:
            pass
        
    #function to perform copy text operation
    def copy_text(self, e):
        try:
            global selected_text
            
            #check to see if keyboard shortcut is used
            if e:
                selected_text = self.root.clipboard_get()
            else:
                if self.text_box.selection_get():
                    selected_text = self.text_box.selection_get()
                    self.root.clipboard_clear()
                    self.root.clipboard_append(selected_text)
        except TclError:
            pass

    #function to perform paste text operation
    def paste_text(self, e):
        try:
            global selected_text
            
            #check to see if keyboard shortcut is used
            if e:
                selected_text = self.root.clipboard_get()
            
            else:
                if selected_text:
                    position = self.text_box.index(INSERT)
                    self.text_box.insert(position, selected_text)
        except TclError:
            pass
    
    #function to implement highlighter
    def add_highlight(self):
        try:
            self.text_box.tag_configure("highlighted", foreground = "red")
            self.text_box.tag_add("highlighted", "sel.first", "sel.last")
        except TclError:
            pass
    
    #function to remove highlight from text
    def remove_highlight(self):
        try:
            self.text_box.tag_configure("highlighted", foreground = "red")
            self.text_box.tag_remove("highlighted", "sel.first", "sel.last")
        except TclError:
            pass

    #function to run python scripts
    def run_script(self):
        try:
            python_program = self.text_box.get(1.0, END)
            exec('print("\\n****************************************Running script****************************************\\n\\n")')
            exec(python_program)
        except TclError:
            pass
            
    def find_text(self):
        try:
            idx = 1.0
            #file_content = self.text_box.get(1.0, END)
            while True:
                idx = self.text_box.search("l", idx, nocase = 1, stopindex = END)
                if not idx:
                    break
                lastidx = '%s+% dc' % (idx, len('l'))
                self.text_box.tag_add('found', idx, lastidx)
                self.text_box.mark_set('insert', idx)
                idx = lastidx
            self.text_box.tag_config("found", foreground = "red")
                
        except TclError:
            pass