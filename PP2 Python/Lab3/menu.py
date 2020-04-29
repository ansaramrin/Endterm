import os
import shutil
def Create_file():
    print('Name this file')
    name=input()
    if os.path.exists(name+".txt"):
        print("The file already exist ")
        return File()
    else:
        with open(name+".txt",'x') as f:
            return(Menu())
        
def Delete_file():
    print('Name of deleting file')
    name=input()
    if os.path.exists(name+".txt"):
        os.remove(name+".txt")
    else:
        print("The file does not exist")
    return Menu()

def  Rename_file():
    print('Print your old name and new name')
    oldname=input()
    newname=input()
    os.rename(oldname+".txt",newname+".txt")
    return Menu()

def Add_content():
    print('''    Name a file that you want add content 
    Print your content ''')
    n=input()
    b=input()
    with open(n+'.txt','a+') as f:
        f.seek(0)
        f.write(b)
    return Menu()

def Rewrite_file():
    print('''    Name a file that you want rewrite content 
    Print your content ''')
    n=input()
    b=input()
    with open(n+'.txt','a+') as f:
        f.seek(0)
        data=f.read(100)
        if len(data)>0:#if file is not empty then i appen \n and take only 10 chars
            f.write("\n")
        f.write(b)
    return Menu()

def Parent_directory():
    path=os.getcwd()
    parent=os.path.dirname(path)
    print(parent)
    return Menu()

def Directory():
    print('''    Print 1 rename directory
    Print 2 number of files in it
    Print 3 number of directories in it
    Print 4 list content of the directory 
    Print 5 add file to this directory
    Print 6 add new directory to this directory  
    Print 7 delete directory 
    Print 8 to back Menu''') 
    n=int(input())
    if n==1:
        return Rename_directory()
    elif n==2:
       return Number_of_files()  
    elif n==3:
        return Number_of_directories() 
    elif n==4:
        return List_content_of_the_directory()
    elif n==5:
        return Add_file_to_this_directory()
    elif n==6:
        return Add_new_directory_to_this_directory()
    elif n==7:
        return Delete()
    elif n==8:
        return Menu()
    else:
        return 0

def Delete():
    print("Name of the deleting file")
    name=input()
    parent=os.getcwd()
    shutil.rmtree(name)
    return Menu()

def Add_file_to_this_directory():
    print('Name this file')
    name=input()
    if os.path.exists(name+".txt"):
        print("The file already exist ")
        return File()
    else:
        with open(name+".txt",'x') as f:
            return(Menu())

def List_content_of_the_directory():
    parent=os.getcwd()
    print(os.listdir(parent))
    return Menu()

def Add_new_directory_to_this_directory():
    print('Create your directory')
    name=input()
    if not os.path.exists(name):
        os.makedirs(name)
        return Menu()
    else:
        print("This directory exists")
        return Directory()

def Rename_directory():
    print('''    Name of the old directory
    Name of the new directory''')
    old=input()
    new=input()
    os.rename(old,new)
    return Menu()
  
def Number_of_files():
    parent=os.getcwd()
    for path,dirs,files in os.walk(parent):
        file_count=len(files)
        print(file_count)
    return Menu()

def Number_of_directories():
    parent=os.getcwd()
    for path,dirs,filed in os.walk(parent):
        print(len(dirs))
    return Menu()
               
def File():
    print('''    Print 1 create a file
    Print 2 delete file
    Print 3 rename file
    Print 4 add content to this file
    Print 5 rewrite content of this file
    Print 6 return to the parent directory
    Print 7 return to the menu ''')
    n=int(input())
    if n==1:
        return Create_file()
    elif n==2:
        return Delete_file()
    elif n==3:
        return Rename_file()
    elif n==4:
        return Add_content()
    elif n==5:
        return Rewrite_file()
    elif n==6:
        return Parent_directory()
    elif n==7:
        return Menu()
    else:
        return 0
   
def Menu():
    print('''    Print the number 1 if you want to work with files 
    Print the number 2 if you want to work directories 
    Print any number to exist''')
    number=int(input())
    if number==1:
        return File()
    elif number==2:
        return Directory()
    else:
        return 0
print(Menu())
 







