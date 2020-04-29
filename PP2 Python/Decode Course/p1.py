from tkinter import *
from PIL import ImageTk,Image

from tkinter import Toplevel
from tkinter import messagebox,ttk
import psycopg2
con=psycopg2.connect(
 database="postgres",
 user="postgres",
 password="Tima010802",
 host="127.0.0.1",
 port="5432"
 )#подключение к бн
cur=con.cursor()
window0=Tk()
window0.title("добро пожаловать")
window0.geometry("300x400")
def postWindow():
    path=["xx.jpg","logo.png"]
    postWin=Toplevel()
    postWin.title("Posts")
    postWin.geometry("1300x700")
    yy=0
    for i in range(len(path)):
        i=Image.open(path[i])
        i=Image.open("bg.jpg")
        img=ImageTk.PhotoImage(i)
        panel=Label(postWin,image=img,width=500,height=700)
        panel.image=img
        panel.place(x=10,y=yy)
        yy=+20
def uiu(user_id):
 windowuiu=Toplevel()
 window2.destroy()
 windowuiu.title("uiu ")
 windowuiu.geometry("300x400")
 get_user_info= "select * from users where id ="+str(user_id)+" "
 cur.execute(get_user_info)
 user= cur.fetchone()
 print(user)
 lbl= ttk.Label(windowuiu, text="Name").place(relx=0.05,rely=0.1)
 lbl= ttk.Label(windowuiu, text=user[1]).place(relx=0.3,rely=0.1)
 lbl= ttk.Label(windowuiu, text="Login").place(relx=0.05,rely=0.2)
 lbl= ttk.Label(windowuiu, text=user[2]).place(relx=0.3,rely=0.2)
 btn22=Button(windowuiu,text="Посты",command=postWindow).pack()

def open():
 global window2
 window2=Toplevel()
 window2.title("вход ")
 window2.geometry("300x400")
 Enterlogin=StringVar()
 EnterPassword=StringVar()
 lbl=Label(window2, text="LOGIN").place(x=30,y=60)
 lbl2=Label(window2, text="пароль",bg="red",fg="black").place(x=30,y=100)
 
 txt=Entry(window2,textvar=Enterlogin,width=10).place(x=150,y=60)
 txt=Entry(window2,textvar=EnterPassword,show="*",width=10).place(x=150,y=100)

 def login():
  login=Enterlogin.get()
  password=EnterPassword.get()
  get_user_sql= """ SELECT * from users where login=%s AND password=%s"""
  cur.execute(get_user_sql, (login,password))
  record=cur.fetchone()
  if record:
   uiu(record[0])
   return
   
  messagebox.showerror("Attention","incorrect password or login")
   

 btn=Button(window2,text="вход",command=login).place(x=100,y=160)

 
 def ll():
  return 0
 window2.mainloop()
def click():
 window3=Toplevel()
 window3.title("uiu")
 window3.geometry("300x400")
 window3.mainloop()
 

def openregister():
 window=Toplevel()
 window.title("рег")
 window.geometry("300x400")
 Entername1=StringVar()
 Enterlogin1=StringVar()
 EnterPassword1=StringVar()
 EnterPassword2=StringVar()
 lbl=Label(window, text="login").grid(column=5,row=3)
 lbl=Label(window, text="name").grid(column=5,row=1)
 lbl2=Label(window, text="пароль",bg="red",fg="black").grid(column=5,row=4)

 lbl3=Label(window, text="повторите пароль",bg="red",fg="black").grid(column=5,row=7)
#lbl.grid(column=0,row=0)
 txt=Entry(window,textvar=Enterlogin1,width=10).grid(column=10,row=3)
 txt=Entry(window,textvar=EnterPassword1,show="*",width=8).grid(column=10,row=4)
 txt=Entry(window,textvar=EnterPassword2,show="*",width=8).grid(column=10,row=7)
 txt=Entry(window,textvar=Entername1,width=10).grid(column=10,row=1)
 def register():
  login=Enterlogin1.get()
  password1=EnterPassword1.get()
  password2=EnterPassword2.get()
  name=Entername1.get()
  if(password1==password2):
   alphavit="qwertyuiopasdfghjklzxcvbnm"
   for x in alphavit:
    for i in password1:
     if i==x:
      count=1

   print("+")
   print("вы прошли регистрацию")
   
   cur.execute("INSERT INTO USERS(NAME,LOGIN,PASSWORD)VALUES(%s, %s, %s)", (name, login, password1))#добавление запрос



   con.commit()#сохранил пользователя в бд

  else:
   messagebox.showerror("massanger","incorrect password")
   return
  if(len(login)<3):
   messagebox.showerror("massanger","недостаточно кол-во букв в login (должно быть больше 3)")
   return
  if(len(login)>10):
   messagebox.showerror("massanger","лимит букв в login 10")
   return
  if(len(password1)<4):
   messagebox.showerror("massanger","пароль должен достигать мин 4 зн")
   return
  if(len(password1)>10):
   messagebox.showerror("massanger","лимит букв в пароле 10")
   return
  print(login)
  print(password1)
  print(password2)
 btn=Button(window,text="najmi",command=register).grid(column=7,row=10)
 


btn=Button(window0,text="вход",command=open).grid(column=100,row=60)
btn=Button(window0,text="рег",command=openregister).grid(column=100,row=90)
window0.mainloop()