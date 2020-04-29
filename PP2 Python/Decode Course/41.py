class Car:
    def __init__(self,model,volume,colour):
        self.model=model
        self.volume=volume
        self.colour=colour
    def display_info(self):
        print("Model:",self.model)
        print("Volume:",self.volume)
        print("Colour:",self.colour)
Mercedes=Car("Mercedes",2,"black")
Mercedes.display_info()
BMW=Car("BMW",4,"white")
BMW.display_info()
Audi=Car("Audi",3,"Grey")
Audi.display_info()