from tkinter import *
from PIL import ImageTk
from tkinter import messagebox, ttk
import mysql.connector

try:
    mydb = mysql.connector.connect(user="root",
                                  password="qwerty",
                                  host="localhost",
                                  port="3306",
                                  database="sys")
    cursor = mydb.cursor()
   

    # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    # sql ='''CREATE TABLE USERS(
    #     Username CHAR,
    #     Login CHAR,
    #     Password CHAR 
    #     )'''
    cursor.execute(sql)
    mydb.close()
    # record = cursor.fetchone()
    # print("You are connected to - ", record, "\n")

    # cursor.execute("CREATE TABLE usersTable (id serial PRIMARY KEY, name VARCHAR , login varchar, password VARCHAR );")
    # print("Created")
    
    # mydb.commit()

except (Exception, mysql.connector.Error) as error:
    print("Error while connecting to Mysql", error)

class Login_System:

    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700")

        # ========All Images====================
        # self.bg_icon=ImageTk.PhotoImage(file="Desktop/bg.jpg")
        # bg_lbl=Label(self.root,image=self.bg_icon).pack()
        # =========Variables====================
        self.login = StringVar()
        self.password1 = StringVar()

        title = Label(self.root, text="Login System", font=("times new roman", 40, "bold"), bg="cadet blue",
                      fg="yellow", bd=10, relief=RIDGE)
        title.place(x=0, y=0, relwidth=1)

        Login_Frame = Frame(self.root, bg="white")
        Login_Frame.place(x=400, y=150)

        loglbl = Label(Login_Frame, text="Login", font=("times new roman", 20, "bold")).grid(row=2, column=0, padx=20,
                                                                                             pady=10)
        txtlogin = Entry(Login_Frame, bd=5, textvar=self.login, relief=RIDGE, font=("", 15)).grid(row=2, column=1,
                                                                                                  padx=20)
        lblpass1 = Label(Login_Frame, text="Password", font=("times new roman", 20, "bold")).grid(row=3, column=0,
                                                                                                  padx=20, pady=10)
        txtpass1 = Entry(Login_Frame, show="*", bd=5, textvar=self.password1, relief=RIDGE, font=("", 15)).grid(row=3,
                                                                                                                column=1,
                                                                                                                padx=20)

        btn_log = Button(Login_Frame, text="Login", command=self.loginHandler, width=15,
                         font=("times new roman", 20, "bold"), bg="blue",
                         fg="red").grid(row=5, column=1, pady=10)

    def loginHandler(self):
        login = self.login.get()
        password = self.password1.get()


        get_user_sql = """ SELECT * from usersTable where login=%s AND password=%s"""
        cursor.execute(get_user_sql, (login, password))

        record = cursor.fetchone()

        if not record:
            messagebox.showerror("Attention", "Incorrect password or login")
            return

        messagebox.showinfo("Success", "Login successful")


def initLogin():
    root = Tk()
    obj = Login_System(root)
    root.mainloop()
