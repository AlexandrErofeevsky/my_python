#Выполнено Ерофеевским и Зотовым

class Client:
    
    def __init__(self, name, number, adress):
        
        self.name = name
        self.number = number
        self.adress = adress
        self.story=0

    def buy_new_car(self, mark, model, year):
        
        self.car = [mark,model,year]
        print(self.name,"купил себе автомобиль марки",mark,"модели",model,year,"года выпуска")
        
class Worker:
    
    def __init__(self,name):
        
        self.name=name
        
    def count(self,client):
        if client.car[0] == "BMW" and client.car[1] =="Sport":
            if client.car[2]<1960:
                self.price=50
            else:
                self.price=40
        elif client.car[0] == "BMW" and client.car[1] =="SUV":
            if client.car[2]<1960:
                self.price=55
            else:
                self.price=45
        elif client.car[0] == "BMW" and client.car[1] =="Muscle":
            if client.car[2]<1960:
                self.price=60
            else:
                self.price=50
        elif client.car[0] == "Porshe" and client.car[1] =="Sport":
            if client.car[2]<1960:
                self.price=65
            else:
                self.price=55
        elif client.car[0] == "Porshe" and client.car[1]=="SUV":
            if client.car[2]<1960:
                self.price=70
            else:
                self.price=60
        elif client.car[0] == "Porshe" and client.car[1] =="Muscle":
            if client.car[2]<1960:
                self.price=75
            else:
                self.price=65
        print("Цена за починку работником",self.name,"автомобиля клиента",client.name,"составит",self.price,"USD")

Alexxx=Client("Alex","88005553535","SPb")
Alexxx.buy_new_car("BMW","SUV",1971)
Max=Worker("Max")
Max.count(Alexxx)
