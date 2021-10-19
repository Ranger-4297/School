# Start import
import tkinter
from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import messagebox
from tkinter import filedialog
# End import

def TopQues():
    root.after(1000, root.withdraw())
    TopQuestions = Toplevel(root)
    TopQuestions.title("Topolgy questions")
    TopQuestions.geometry("500x300")
    TopQuestions.resizable(0,0)
    TopQuestions.config(bg="#2f3136")

def Ll():
    root.after(1000, root.withdraw())
    Ll = Toplevel(root)
    Ll.title("Level questions")
    Ll.geometry("500x300")
    Ll.resizable(0,0)
    Ll.config(bg="#2f3136")

# GUI
root = Tk()
root.title("Revision") # Name of window
root.geometry("350x50") # Size of window
root.resizable(0,0) # Prevent window resizing
root.config(bg="#2f3136") # Window background

btnTopologies=Button(root, text="Topologies", command=TopQues, bg="#2f3136", fg="white", activebackground="grey", height="3", width="10").place(x=0, y=0)

btnLl=Button(root, text="High/low level languages", command=Ll, bg="#2f3136", fg="white", activebackground="grey", height="3").place(x=80, y=0)

btnProto=Button(root, text="Protocols", command=Ll, bg="#2f3136", fg="white", activebackground="grey", height="3").place(x=225, y=0)

btnHWare=Button(root, text="Hardware", command=Ll, bg="#2f3136", fg="white", activebackground="grey", height="3").place(x=290, y=0)

# load GUI
root.mainloop()