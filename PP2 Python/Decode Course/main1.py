from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox,ttk
#import psycopg2


# con = psycopg2.connect(
#  database="postgres",
#  user="postgres",
#  password="qwerty",
#  host="127.0.0.1",
#  port="5432"
#  )


window = Tk()
window.title("welcome to messenger")
window.geometry("300x400")


# def newwindow():
#     window2=Tk()
#     window.destroy()
#     window2.title("LOGIN")
#     window2.geometry("300x400")
#     lbl1 = Label(window2, text="LOGIN", font=("Arial Bold", 30), bg="red", fg="black").place(x=100, y=0)
#     lbl2 = Label(window2, text="Login").place(x=20, y=50)
#     lbl3 = Label(window2, text="password").place(x=20, y=85)

#     txt1 = Entry(window2, width=20).place(x=120, y=50)
#     txt2 = Entry(window2, width=20).place(x=120, y=80)

#     btn1 = Button(window2, text="Enter", command=ret).place(x=150, y=250)


def openRegisterWindow():
    window3=Toplevel()
    # window.destroy()
    window3.title("REGISTER")
    window3.geometry("400x600")
    EnterName=StringVar()
    EnterLogin=StringVar()
    EnterPassword1=StringVar()
    EnterPassword2=StringVar()
    lbl1 = Label(window3, text="Register", font=("Arial Bold", 20), bg="red", fg="black").place(x=100, y=0)
    lbl2 = Label(window3, text="Login").place(x=20, y=50)
    lbl3 = Label(window3, text="password").place(x=20, y=85)
    lbl4 = Label(window3, text="name").place(x=20, y=30)
    lbl5 = Label(window3,text="repeat password").place(x=20,y=110)
    txt1 = Entry(window3,textvar=EnterLogin, width=20).place(x=160, y=50)
    txt2 = Entry(window3,textvar=EnterPassword1,show='*', width=20).place(x=160, y=80)
    txt3 = Entry(window3,textvar=EnterName, width=20).place(x=160, y=30)
    txt4 = Entry(window3,textvar=EnterPassword2,show='*', width=20).place(x=160, y=110)

    def register():
        name=EnterName.get()
        login=EnterLogin.get()
        password1=EnterPassword1.get()
        password2=EnterPassword2.get()

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

    btn1 = Button(window3, text="Register", command=register).place(x=150, y=250)

#lbl1.grid(column=0,row=0)
#lbl2.grid(column=1,row=0)
btn1 = Button(window,text="register",command=openRegisterWindow).place(x=100,y=100)
# btn2 = Button(window,text="login",command=newwindow).place(x=100,y=150)



window.mainloop()