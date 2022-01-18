#Start import libraries
from tkinter import *
from tkinter import messagebox
#End import

#Start command definition
def Ok():
    uname = e1.get
    pword = e2.get()
#End command definition

#Start password checker
    #Start If Blank
    if uname == "" and pword == "":
        messagebox.showerror("Error", "Blank not allowed")
        #End If Blank

    #Start Else If Correct
    elif uname == "Test" and pword == "Josh":
        messagebox.showinfo("", "Login Success")
        root.destroy() #Closes GUI
        #End Else If Correct

    #Start if Else
    else:
        messagebox.showerror("Error", "Incorrect username and/or password")
        #End Else
#End password checker

#Start page setup
root = Tk()
root.title("Login") # Name of window
root.geometry("500x310") # Size of window
root.resizable(0,0) #If (0,0) then NOT resizable
root.configure(bg="#36393f") #Background colour
global e1
global e2
#End page setup

#Start title/heading
title=Label(root, text="Login Panel", font=("calibri",40,"bold"),bd=10,bg="#2f3136",relief=RIDGE)
title.place(x=0,y=0,relwidth=1)
#End title/heading

#Start Password+Username labels
label1=Label(root, text="Username", fg="white", bg="#36393f")
label2=Label(root, text="Password", fg="white", bg="#36393f")
label1.place(x=10, y=100)
label2.place(x=10, y=130)
#End Password+Username labels

#Start Text/Input boxes
e1 = Entry(root)
e1.place(x=140, y=100)

e2 = Entry(root)
e2.configure(show="*")
e2.place(x=140, y=130)
#Ends Text/Input boxes

#Start Login button
Button(root, text="Login", command=Ok ,height = 1, width = 11)
#End Login button

#Run/Open GUI
root.mainloop()
