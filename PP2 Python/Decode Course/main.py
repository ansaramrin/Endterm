from tkinter import *
def click():
    window2=Tk()
    window.destroy()
    window2.title("Lets start")
    window2.geometry("800x600")
    lbl2=Label(window2,text="Login",font=("Arial Bold",30),bg="green",fg="black").pack()
    lbl3=Label(window2,text="Login",font=("Arial Bold",30),bg="blue",fg="black").place(x=100,y=50)
    lbl4=Label(window2,text="Password",font=("Arial Bold",30),bg="blue",fg="black").place(x=80,y=100)
    txt2=Entry(window2,width=10).pack()
    txt3=Entry(window2,width=10).pack()

    window3=Tk()
    window2.destroy()
    window3.title("Very good")
    window3.geometry("800x600")
    lbl5=Label(window3,text="Register",font=("Arial Bold",30),bg="red",fg="black").pack()
    lbl6=Label(window3,text="Name",font=("Arial Bold",30),bg="blue",fg="black").place(x=100,y=50)
    lbl7=Label(window3,text="Login",font=("Arial Bold",30),bg="blue",fg="black").place(x=80,y=100)
    lbl6=Label(window3,text="Password",font=("Arial Bold",30),bg="blue",fg="black").place(x=120,y=150)
    lbl7=Label(window3,text="Confirm Password",font=("Arial Bold",30),bg="blue",fg="black").place(x=110,y=130)
    txt4=Entry(window3,width=10).pack()
    txt5=Entry(window3,width=10).pack()
    txt6=Entry(window3,width=10).pack()
    txt7=Entry(window3,width=10).pack()
    
window = Tk()
window.title("Welcome to our soc net")
window.geometry("300x400")
btn=Button(window,text="Login",command=click).pack()
btn1=Button(window,text="Register",command=click).pack()
    btn2=Button(window2,text="Entry",command=click).pack()
    btn3=Button(window3,text="Entry",command=click).pack()  

# lbl.grid(column=0,row=0)
# lbl2.grid(column=1,row=0)



window.mainloop()