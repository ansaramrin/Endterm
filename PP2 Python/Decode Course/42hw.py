class Books:
    def __init__(self,name,author,year):
        self.name=name
        self.author=author
        self.year=year
    def print_info(self):
        print("name is",self.name)
        print("author is",self.author)
        print("year is",self.year)
    def returnName(self):
    	return self.name
books=[]
books=[]
while True:		
	print("-------------------")
	print("1.Добавть книгу")
	print("2.Удалить книгу")
	print("3.Все книги")
	print("4.Выход")
	x=int(input())
	if x==1:
		name=input("Enter name: ")
		author=input("Enter author: ")
		year = int(input("Enter year: "))
		books.append(Books(name,author,year))
		print("Книга Добавлена")
	elif x==2:
		delName=input("Напишите название книги которую вы хотите удалить")
		for i in range(len(books)):
			print(books[i].returnName())
			# if books[i].returnName()==delName:
			# 	print(books[i].print_info())
	elif x==3:
		for i in range(len(books)):
			books[i].print_info()
	elif x==4:
		break
	else:
		print("Error,incorrect data")