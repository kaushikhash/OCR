from tkinter import * 
from tkinter.ttk import *
from tkinter import filedialog

import os

import ocr as o

top = Tk()   
top.title('Image to Text converter')
top.geometry("450x300")  



#menu 
menubar = Menu(top)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = top.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)




def file_opener():
    global newpath
    filepath= filedialog.askopenfilename()
    onlyfilename = os.path.abspath(filepath)
    newpath = onlyfilename.replace(os.sep, '/')
    mylabel.config(text=newpath)
    
def text_box(output):
    txt.insert(END,output)
    
    
def converter():
    global output
    output = o.ocr(str(newpath))
    text_box(output)
    
    
    
button = Button (top,text='Browse an image', command=file_opener)
button.grid(row=0,column=0)

convert = Button (top,text='convert', command=converter)
convert.grid(row=1,column=0)

mylabel = Label(top, text="Your chosen file path will be displayed here")
mylabel.grid(row=0,column=1)

txt = Text(top,height=25,width=100)
txt.grid(row=15,column=0)


top.config(menu = menubar)
top.mainloop() 




