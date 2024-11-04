from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0,END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='untitled.txt',defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad By Rahul_Sarraf")

if __name__ == '__main__':
    root = Tk()
    root.geometry("655x788")
    root.title("Notepad")
    root.wm_iconbitmap("R:\MCA(24-26)\Html\Project3(ToDo_List)\images\icon.png")

    #Text Area
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(fill="both", expand=True)

    menubar = Menu(root)
    #Fist 
    FileMenu = Menu(menubar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    menubar.add_cascade(label="File", menu=FileMenu)
    root.config(menu=menubar)

    #Second
    EditMenu = Menu(menubar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit", menu=EditMenu)
    root.config(menu=menubar)

    #Third
    HelpMenu = Menu(menubar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    menubar.add_cascade(label="Help", menu=HelpMenu)
    root.config(menu=menubar)

    #Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side="right",fill="y")
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()