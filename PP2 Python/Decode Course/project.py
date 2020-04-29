from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox,ttk
import mysql.connector

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700")

        #========All Images====================
        self.bg_icon=ImageTk.PhotoImage(file="Desktop/bg.jpg")
        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        #=========Variables====================
        self.name=StringVar()
        self.login=StringVar()
        self.password1=StringVar()
        self.password2=StringVar()


        title=Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg="cadet blue",fg="yellow",bd=10,relief=RIDGE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=400,y=150)
        
        lbluser=Label(Login_Frame,text="Username",font=("times new roman",20,"bold")).grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame,bd=5,textvar=self.name,relief=RIDGE,font=("",15)).grid(row=1,column=1,padx=20)
        loglbl=Label(Login_Frame,text="Login",font=("times new roman",20,"bold")).grid(row=2,column=0,padx=20,pady=10)
        txtlogin=Entry(Login_Frame,bd=5,textvar=self.login,relief=RIDGE,font=("",15)).grid(row=2,column=1,padx=20)
        lblpass1=Label(Login_Frame,text="Password",font=("times new roman",20,"bold")).grid(row=3,column=0,padx=20,pady=10)
        txtpass1=Entry(Login_Frame,bd=5,textvar=self.password1,show='*',relief=RIDGE,font=("",15)).grid(row=3,column=1,padx=20)
        lblpass2=Label(Login_Frame,text="Confirm Password",font=("times new roman",20,"bold")).grid(row=4,column=0,padx=20,pady=10)
        txtpass2=Entry(Login_Frame,bd=5,textvar=self.password2,show='*',relief=RIDGE,font=("",15)).grid(row=4,column=1,padx=20)

        btn_log=Button(Login_Frame,text="Login",width=15,font=("times new roman",20,"bold"),bg="white",fg="red").grid(row=5,column=1,pady=10)
        btn1 = Button(self.root1, command=showimages).place(x=150, y=250)
 
        
    def Login_fill(self):
        name=self.name.get()
        login=self.login.get()
        password1=self.password1.get()
        password2=self.password2.get()

        print(name)
        print(login)
        print(password1)
        print(password2)  

        if len(name)>=6:
            print("OK")
        else:
            messagebox.showerror("Attention","Incorrect name")
            if len(login)>=6:
                print("OK")
            else:
                messagebox.showerror("Attention","Incorrect login")
                if len(password1)>=8:
                    print("OK")
                else:
                    messagebox.showerror("Attention","Incorrect Password")
                    if len(password2)>=8:
                        print("OK")
                    else:
                        messagebox.showerror("Attention","Incorrect password")
                        if password1==password2:
                            print("OK")
                        else:
                            messagebox.showerror("Attention","Incorrect password")
        print(name)
        print(login)
        print(password1)
        print(password2) 
    def showimages(self,root1): 
        self.root1=Toplevel()
        self.root1.title("Images")
        self.root1.geometry("1350x700")


root=Tk()
obj=Login_System(root)
root.mainloop()