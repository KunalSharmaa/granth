from tkinter import *
from tkinter import filedialog
from commands import *
from menus import *
from bindings import *

root = Tk()
root.title('ScratchPad')
root.geometry('1200x660')
    
#create main frame
main_frame = Frame(root)
main_frame.pack(pady = 5)

#create top level main menu
main_menu = Menu(root)
root.config(menu = main_menu)

#create scrollbar for text box
text_scroll = Scrollbar(main_frame)
text_scroll.pack(side = RIGHT, fill = Y)

#create text box
text_box = Text(main_frame, width = 97, height = 25, font = ("Helvetica", 16), selectbackground = "lightblue", selectforeground = "black", undo = True, yscrollcommand = text_scroll.set)
text_box.pack()

#configure scrollbar with text box
text_scroll.config(command = text_box.yview)

#create status bar at the bottom
status_bar = Label(root, text = 'Ready        ', anchor = E)
status_bar.pack(fill = X, side = BOTTOM, ipady = 5)

commands = Commands(root, main_frame, text_box, status_bar)

#create menus
menus = Menus(root, main_frame, text_box, status_bar, main_menu, commands)
menus.create_file_menu()
menus.create_edit_menu()
menus.create_tools_menu()

#update keyboard bindings
bindings = Bindings(root, commands)
bindings.update()

root.mainloop()