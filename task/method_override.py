#***********************************************************************************************************

#*********************METHOD OVERRIDING********************************************************************

class Animal:
    def move(self):
        print("Animal walks")


class Frog(Animal):
    def move(self):
        print("Frog jumping")

frog = Frog()
frog.move()


#vehicle 


class Vehicle :
    def start(self):
        print("vehicle is starting")

class Car(Vehicle):
    def start(self):
        print(" car starting using key")

class Electric_bike:
    def start(self):
        print(" bike starting using push bottun")


car = Car()
electric_bike = Electric_bike()

car.start()
electric_bike.start()

