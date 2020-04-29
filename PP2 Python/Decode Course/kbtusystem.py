from tkinter import *
import tkinter.messagebox

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Managemnet Systems")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")
        self.root.config(bg="cadet blue")
        ID=StringVar()
        Name=StringVar()
        Surname=StringVar()
        Age=StringVar()
        Faculty=StringVar()
        Gender=StringVar()
        Mobile=StringVar()
        #=================================Frame=====================================
        MainFrame=Frame(self.root,bg="cadet blue")
        MainFrame.grid()

        TitleFrame=Frame(MainFrame,bd=2,padx=54,pady=8,bg="Ghost White",relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,font=('arial',47,'bold'),text="Student Managemnet Systems",bg="Ghost White")
        self.lblTitle.grid()


if __name__=='__main__':
    root=Tk()
    app=Student(root)
    root.mainloop()



