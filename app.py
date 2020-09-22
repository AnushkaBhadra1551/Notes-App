from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

class Notepad(tk.Tk):
    def __init__(self):

        self.root=Tk()
        #Setting icon
        self.root.iconbitmap(r'notepad_icon_FC9_icon.ico')

        #Application Title
        self.root.title("Untitled - Notepad")

        self.root.geometry("700x500")

        self.root.configure(background='white')


        self.loadHomeGUI()
        self.headerMenu()

        self.root.mainloop()
        global nfiles
        nfiles = False

    def loadHomeGUI(self):

        self.clear()
        self.title=Label(self.root)


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def headerMenu(self):

        self.clear()

        menu = Menu(self.root)
        self.root.config(menu=menu)

        filemenu = Menu(menu,tearoff=0)        #file menu
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New",command=lambda:self.new())
        filemenu.add_command(label="Open",command=lambda:self.open())
        filemenu.add_command(label="Save",command=lambda:self.save())
        filemenu.add_command(label="Save As", command=lambda: self.saveas())
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=lambda:self.exit())

        editmenu = Menu(menu,tearoff=0)       #edit menu
        menu.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Cut",command=lambda:self.cut())
        editmenu.add_command(label="Copy",command=lambda:self.copy())
        editmenu.add_command(label="Paste",command=lambda:self.paste())


        helpmenu = Menu(menu,tearoff=0)      #help menu
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About Notepad",command=lambda:self.about())

        #Adding scrollbars and text area
        self.yscrollbar = Scrollbar(self.root)
        self.yscrollbar.pack(side=RIGHT, fill=Y)

        self.xscrollbar = Scrollbar(self.root,orient='horizontal')
        self.xscrollbar.pack(side=BOTTOM, fill=X)

        self.textarea=Text(self.root,yscrollcommand=self.yscrollbar.set,wrap="none",xscrollcommand=self.xscrollbar.set)
        self.textarea.pack(fill=BOTH)

        self.yscrollbar.config(command=self.textarea.yview)
        self.xscrollbar.config(command=self.textarea.xview)

    def new(self):  #new_menu

        self.file = None
        self.root.title("Untitled - Notepad")
        self.textarea.delete(1.0,END)


    def open(self):   #open_menu
        self.file=askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents","*.txt")])
        global nfiles
        nfiles=self.file
        if self.file=="":
            self.file=None
        else:
            self.root.title(os.path.basename(self.file)+ " - Notepad")
            self.textarea.delete(1.0,END)
            self.files=open(self.file,"r")
            self.textarea.insert(1.0, self.files.read())
            self.files.close()

    def save(self):     #save_menu
        global nfiles
        if nfiles:
            self.newfile = open(nfiles, "w")
            self.newfile.write(self.textarea.get(1.0, END))
            self.newfile.close()
            messagebox.showinfo("Notepad", "Saved")

        else:
            self.saveas()


    def saveas(self):      #saveas_menu
        self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),("HTML Files","*.html"), ("Python Files","*.py")])
        if self.file:
            self.root.title(os.path.basename(self.file) + " - Notepad")
            self.newfile = open(self.file, "w")
            self.newfile.write(self.textarea.get(1.0, END))
            self.newfile.close()
        else:
            self.file=None

    def exit(self):     #exit_menu
        self.root.destroy()

    def cut(self):      #cut_menu
        self.textarea.event_generate(("<<Cut>>"))

    def copy(self):     #copy_menu
        self.textarea.event_generate(("<<Copy>>"))

    def paste(self):    #paste_menu
        self.textarea.event_generate(("<<Paste>>"))

    def about(self):    #about_menu
        messagebox.showinfo("Notepad","Notepad by Anushka")


        


note=Notepad()