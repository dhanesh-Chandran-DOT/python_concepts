#******************************************************

#


class Animal:
    def eat(self):
        print("Animal eats")


class Walker:
    def walk(self):
        print("walks")


class Dog(Animal,Walker):
    def bark(self):
        print("barks")

dog = Dog()
dog.eat()
dog.walk()
dog.bark()


# camara class taks

class Camera:
    def take_photo(self):
        print("capturing photos")

class Call:
    def make_call(self):
        print("calling friends")

class Smartphone(Camera, Call):
    def internet(self):
        print("browsing internet")


phone = Smartphone()
phone.take_photo()
phone.make_call()
phone.internet()     






#muti task




class Mediaplayer:
    def play_video(self):
        print("playing video")

class Internetdevice:
    def connect_wifi(self):
        print("connet to wifi")

class SmartTV(Mediaplayer,Internetdevice):
    def change_channel(self):
        print("changing TV channel")

tv = SmartTV()
tv.play_video()
tv.connect_wifi()
tv.change_channel

    