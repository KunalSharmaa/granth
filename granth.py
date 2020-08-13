from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('ScratchPad')
root.geometry('1200x660')

global opened_text_file
opened_text_file = False

global selected_text
selected_text = False

#function to create new file
def new_file():
    #delete any existing text
    text_box.delete(1.0, END)
    
    #update status bars
    root.title('New File - ScratchPad')
    status_bar.config(text = "New File        ")
    
    global opened_text_file
    opened_text_file = False

#function to Open existing files    
def open_file():
    #delete any existing text
    text_box.delete(1.0, END)
    
    #grab filename
    global opened_text_file
    opened_text_file = filedialog.askopenfilename(initialdir = "D:/projects/", title = "Open File", filetypes = (("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py")))
    
    #update status bars
    filename = opened_text_file
    status_bar.config(text = f'{filename}        ')
    filename = filename.replace("D:/projects/", "")
    root.title(f'{filename} - ScratchPad')
    
    #open the file
    with open(opened_text_file, 'r') as fh:
        file_content = fh.read()
    
    #add file content to text box
    text_box.insert(END, file_content)

#function to save overwritten files    
def save_file():
    global opened_text_file
    if opened_text_file:
        with open(opened_text_file, 'w') as fh:
            fh.write(text_box.get(1.0, END))
        status_bar.config(text = f'Saved: {opened_text_file}')
    else:
        save_file_as()
    

#function to save new files
def save_file_as():
    text_file = filedialog.asksaveasfilename(defaultextension = ".*", initialdir = "D:/projects/", title = "Save File", filetypes = (("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py")))
    
    #check if file exists, since we have the option of cancel as well in the dialog box
    if text_file:
        #update status bars
        filename = text_file
        status_bar.config(text = f' Saved: {filename}        ')
        filename = filename.replace("D:projects/", "")
        root.title(f'{filename} - ScratchPad')
        
        #save the file
        with open(text_file, 'w') as fh:
            fh.write(text_box.get(1.0, END))
        
#function to perform cut text operation
def cut_text(e):
    global selected_text
    
    #check to see if keyboard shortcut is used
    if e:
        selected_text = root.clipboard_get()
    
    else:
        if text_box.selection_get():
            selected_text = text_box.selection_get()
            text_box.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected_text)
    
#function to perform copy text operation
def copy_text(e):
    global selected_text
    
    #check to see if keyboard shortcut is used
    if e:
        selected_text = root.clipboard_get()
    else:
        if text_box.selection_get():
            selected_text = text_box.selection_get()
            root.clipboard_clear()
            root.clipboard_append(selected_text)
        

#function to perform paste text operation
def paste_text(e):
    global selected_text
    
    #check to see if keyboard shortcut is used
    if e:
        selected_text = root.clipboard_get()
    
    else:
        if selected_text:
            position = text_box.index(INSERT)
            text_box.insert(position, selected_text)
        
#create main frame
main_frame = Frame(root)
main_frame.pack(pady = 5)

#create scrollbar for text box
text_scroll = Scrollbar(main_frame)
text_scroll.pack(side = RIGHT, fill = Y)

#create text box
text_box = Text(main_frame, width = 97, height = 25, font = ("Helvetica", 16), selectbackground = "lightblue", selectforeground = "black", undo = True, yscrollcommand = text_scroll.set)
text_box.pack()

#configure scrollbar with text box
text_scroll.config(command = text_box.yview)

#create menu
main_menu = Menu(root)
root.config(menu = main_menu)

#create file menu
file_menu = Menu(main_menu, tearoff = False)
main_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = new_file)
file_menu.add_command(label = "Open", command = open_file)
file_menu.add_command(label = "Save", command = save_file)
file_menu.add_command(label = "Save As", command = save_file_as)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)

#create edit menu
edit_menu = Menu(main_menu, tearoff = False)
main_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut      (Ctrl+x)", command = lambda: cut_text(False))
edit_menu.add_command(label = "Copy     (Ctrl+c)", command = lambda: copy_text(False))
edit_menu.add_command(label = "Paste    (Ctrl+v)", command = lambda: paste_text(False))
edit_menu.add_command(label = "Undo")
edit_menu.add_command(label = "Redo", command = root.quit)

#create status bar at the bottom
status_bar = Label(root, text = 'Ready        ', anchor = E)
status_bar.pack(fill = X, side = BOTTOM, ipady = 5)

#edit bindings
root.bind('<Control-x>', cut_text)
root.bind('<Control-c>', copy_text)
root.bind('<Control-v>', paste_text)

root.mainloop()