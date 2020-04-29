import os

def parent_directory():
    path=os.getcwd()
    parent=os.path.dirname(path)
    print(parent)
    return menu()

def delete_file():
    print('Name of deleting file')
    name=input()
    if os.path.exists(name+".txt"):
        os.remove(name+".txt")
    else:
        print("Not exist")
    return menu()

def  rename_file():
    print('Print your old name and new name')
    old_name=input()
    new_name=input()
    os.rename(old_name+".txt",new_name+".txt")
    return menu()

def add_content():
    print('''    Name a file that you want add content 
    Print your content ''')
    n=input()
    m=input()
    with open(n+'.txt','a+') as f:
        f.write(m)
    return menu()

def rewrite_file():
    print('''    Name a file that you want rewrite content 
    Print your content ''')
    n=input()
    with open(n+'.txt', mode='w') as file:  
        file.write(n)
    return menu()

def directory():
    print('''    Print 1 rename directory
    Print 2 number of files in it
    Print 3 number of directories in it
    Print 4 list content of the directory 
    Print 5 add file to this directory
    Print 6 add new directory to this directory   
    Print 7 to back Menu''') 
    n=int(input())
    if n==1:
        return rename_directory()
    elif n==2:
       return number_of_files()  
    elif n==3:
        return number_of_directories() 
    elif n==4:
        return list_content_of_the_directory()
    elif n==5:
        return add_file_to_this_directory()
    elif n==6:
        return add_new_directory_to_this_directory()
    elif n==7:
        return menu()
    else:
        return 0
def add_file_to_this_directory():
    print('Which file')
    file=input()
    if os.path.exists(file+".txt"):
        print("Exist ")
        return file()
    else:
        with open(file+".txt",'x') as f:
            return(menu())

def list_content_of_the_directory():
    basepath = os.getcwd()
    with os.scandir(basepath) as entries:
        for entry in entries:   
            if entry.is_file():
                print(entry.name)


def add_new_directory_to_this_directory():
    print('Add your directory')
    name=input()
    if not os.path.exists(name):
        os.makedirs(name)
        return menu()
    else:
        print("Exists")
        return directory()

def rename_directory():
    print('''    Name of the old directory
    Name of the new directory''')
    old=input()
    new=input()
    os.rename(old,new)
    return menu()
  
def number_of_files():
    parent=os.getcwd()
    for path,directories,files in os.walk(parent):
        num=len(files)
        print(num)
    return menu()

def number_of_directories():
    parent=os.getcwd()
    for path,directories,files in os.walk(parent):
        print(len(directories))
    return menu()
               
def file():
    print('''
    Print 1 delete file
    Print 2 rename file
    Print 3 add content to this file
    Print 4 rewrite content of this file
    Print 4 return to the parent directory
    Print 6 return to the menu ''')
    n=int(input())
    if n==1:
        return delete_file()
    elif n==2:
        return rename_file()
    elif n==3:
        return add_content()
    elif n==4:
        return rewrite_file()
    elif n==5:
        return parent_directory()
    elif n==6:
        return menu()
    else:
        return 0
def menu():
    print('''-------------------
    Press 1 to work with files
    Press 2 to work with directories
    -------------------------''')
    n=int(input())
    if n==1:
        return file()
    elif n==2:
        return directory()
    else:
        return 0
print(menu())
   

 