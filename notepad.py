# importing required packages and libraries

from tkinter import Tk, Menu
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog, simpledialog
from tkinter.scrolledtext import ScrolledText

# the root widget
root = Tk()
root.title("Ryan's Notepad")
root.resizable(0, 0)

# creating scrollable notepad window
notepad = ScrolledText(root, width=90, height=40)
fileName = ' '


# defining functions for commands
def cmdNew():  # file menu New option
    global fileName
    if len(notepad.get('1.0', tk.END + '-1c')) > 0:
        if messagebox.askyesno("Ryan's Notepad", "Do you want to save changes?"):
            cmdSave()
        else:
            notepad.delete(0.0, tk.END)
    root.title("Ryan's Notepad")


def cmdOpen():  # file menu Open option
    fd = filedialog.askopenfile(parent=root, mode='r')
    t = fd.read()  # t is the text read through filedialog
    notepad.delete(0.0, tk.END)
    notepad.insert(0.0, t)


def cmdSave():  # file menu Save option
    fd = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if fd is not None:
        data = notepad.get('1.0', tk.END)
    try:
        fd.write(data)
    except Exception:
        messagebox.showerror(title="Error", message="Not able to save file!")


def cmdSaveAs():  # file menu Save As option
    fd = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = notepad.get(0.0, tk.END)  # t stands for the text gotten from notepad
    try:
        fd.write(t.rstrip())
    except Exception:
        messagebox.showerror(title="Error", message="Not able to save file!")


def cmdExit():  # file menu Exit option
    if messagebox.askyesno("Notepad", "Are you sure you want to exit?"):
        root.destroy()


def cmdCut():  # edit menu Cut option
    notepad.event_generate("<<Cut>>")


def cmdCopy():  # edit menu Copy option
    notepad.event_generate("<<Copy>>")


def cmdPaste():  # edit menu Paste option
    notepad.event_generate("<<Paste>>")


def cmdClear():  # edit menu Clear option
    notepad.event_generate("<<Clear>>")


def cmdFind():  # edit menu Find option
    notepad.tag_remove("Found", '1.0', tk.END)
    find = simpledialog.askstring("Find", "Find what:")
    if find:
        idx = '1.0'  # idx stands for index
    while 1:
        idx = notepad.search(find, idx, nocase=1, stopindex=tk.END)
        if not idx:
            break
        lastidx = '%s+%dc' % (idx, len(find))
        notepad.tag_add('Found', idx, lastidx)
        idx = lastidx
    notepad.tag_config('Found', foreground='white', background='blue')
    notepad.bind("<1>", click)


def click(event):  # handling click event
    notepad.tag_config('Found', background='white', foreground='black')


def cmdSelectAll():  # edit menu Select All option
    notepad.event_generate("<<SelectAll>>")


def cmdTimeDate():  # edit menu Time/Date option
    now = datetime.now()
    # dd/mm/YY H:M:S
    dtString = now.strftime("%d/%m/%Y %H:%M:%S")
    label = messagebox.showinfo("Time/Date", dtString)  # noqa: F841


def cmdAbout():  # help menu About option
    label = messagebox.showinfo("About Notepad", "Notepad by - Ryan") #noqa: F841


# notepad menu items
notepadMenu = Menu(root)
root.configure(menu=notepadMenu)

# file menu
fileMenu = Menu(notepadMenu, tearoff=False)
notepadMenu.add_cascade(label='File', menu=fileMenu)

# adding options in file menu
fileMenu.add_command(label='New', command=cmdNew)
fileMenu.add_command(label='Open...', command=cmdOpen)
fileMenu.add_command(label='Save', command=cmdSave)
fileMenu.add_command(label='Save As...', command=cmdSaveAs)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=cmdExit)

# edit menu
editMenu = Menu(notepadMenu, tearoff=False)
notepadMenu.add_cascade(label='Edit', menu=editMenu)

# adding options in edit menu
editMenu.add_command(label='Cut', command=cmdCut)
editMenu.add_command(label='Copy', command=cmdCopy)
editMenu.add_command(label='Paste', command=cmdPaste)
editMenu.add_command(label='Delete', command=cmdClear)
editMenu.add_separator()
editMenu.add_command(label='Find...', command=cmdFind)
editMenu.add_separator()
editMenu.add_command(label='Select All', command=cmdSelectAll)
editMenu.add_command(label='Time/Date', command=cmdTimeDate)

# help menu
helpMenu = Menu(notepadMenu, tearoff=False)
notepadMenu.add_cascade(label='Help', menu=helpMenu)

# adding options in help menu
helpMenu.add_command(label='About Notepad', command=cmdAbout)
notepad.pack()
root.mainloop()

