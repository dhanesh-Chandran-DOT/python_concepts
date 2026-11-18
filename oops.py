# #****************************************************************************************

# student_name = 'dhanesh'
# age = 26
 
# student_name1 = 'raju'
# age_1 = 22

# student_name2 = 'theju'
# age_2 = 23

# student_name3 = 'saju'
# age_3 = 19

# student_name4 = 'jesi'
# age_4 = 20

# print(student_name, age,student_name1,age_1,student_name2,age_2,student_name3,age_3,student_name4,age_4)










# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# student_name1 = student('jhon',23 )
# student_name2 = student('jerin',55)
# student_name3 = student('rajesh',33)
# student_name4 = student('babu',32)

# print(student_name1.name,student_name1.age,student_name2.name ,student_name2.age,student_name3.name, student_name3.age, student_name4.name, student_name4.age)



# #5 books


# class Book():
#     def __init__(self,name,author,pages,year):
#         self.name =name
#         self.author =author
#         self.pages = pages
#         self.year =year


# book1 = Book('half girlfriend','leo',300,2010)
# book2 = Book('alfa','grace',400,2000)
# book3 = Book('JOrge','seer',302,2022)
# book4 = Book('science','a',200,2003)

# print(book1.name,book1.author,book1.pages,book1.year)
# print(book2.name,book2.author,book2.pages,book2.year)
# print(book3.name,book3.author,book3.pages,book3.year)
# print(book4.name,book4.author,book4.pages,book4.year)


# #employ


# class Employee():
#     # class attribute
#     age = 10

#     def __init__(self,name,sal,id_no,job_roll,joining_date):
#         self.name = name
#         self.sal = sal
#         self.id_no = id_no
#         self.job_roll = job_roll
#         self.joinin_date = joining_date

#     def display_details(self):
#         print(self.name,self.sal,self.id_no,self.job_roll,self.joinin_date)


# emp1 = Employee('hari',25000,21,'trainy','11/2/2026')
# emp2 = Employee('rahul',13000,12,'team_leader','12/7/2023')
# emp3 = Employee('JOJI',50000,555,'HR','10/8/2003')
# emp4 = Employee('krishna',100000,36,'manager','30/9/2001')
# emp5 = Employee('kishore',150000,23,'asstmanager','25/10/2008')    

# emp1.display_details()
# emp2.display_details()
# emp3.display_details()
# emp4.display_details()
# emp5.display_details()

# print(Employee.age)



# class student:
#     count = 0

#     def __init__(self,name,age,height):
#         self.name = name
#         self.age = age
#         self.height = height
#     # increment count by 1
#         student.count = student.count + 1

#     def display_count(self):
#         print(student.count)    
# student_name1 = student('john',23,2001)
# student_name2 = student('jiji',56,2000)
# student_name3 = student('jorge',22,1998)
# student_name3.display_count()


# #


# class Animal:
#     def __init__(self,has_leg):
#         self.has_leg = has_leg

# class Dog(Animal):
#     pass

# dog = Dog(has_leg = 'yes')


# print('the dogs has 4 legs',Dog.has_leg)


# #create 4 classes


# class Animal:
#     def __init__(self,sleep,eat):
#         self.sleep = sleep
#         self.eat = eat
#         pass


# class Dog(Animal):
#     def __init__(self,sleep,eat):
#         super().__init__(sleep,eat)                     # it inherit the data from parent
#         self.speak = 'bow'



# class Cat(Animal):
#     def __init__(self,sleep,eat):
#         super().__init__(sleep,eat)
#         self.speak = 'meow'

# dog = Dog(sleep='yes', eat='yes')
# cat = Cat(sleep='yes',eat= 'yes')

# print(Dog.speak,Dog.sleep,Dog.eat)
# print(Cat.speak,Cat.sleep,Cat.eat)






# task*****************************************


# class Animal:
#     def __init__(self,name,age):

#         self.name = name
#         self.age = age
#         pass


#     def Eat(self):                                                          # method is writing inside the function
#         print("the animal is eating")

# class Dog(Animal):
  
#     def bark(self):
#        return "Woof"



# class Cat(Animal):
    
#     def meow(self):
#         return "Meow"                       # to avoid none

# dog = Dog(name = 'yes',age = 'yes',)        # objects
# cat = Cat(name = 'yes', age = 'yes')

# print(dog.name,dog.age,dog.bark())
# print(cat.name,cat.age,cat.meow())


# task7 


# class Person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         pass

#     def display(self):
#         print(self.name, self.age)  # it prints the name and age from the parent 


# class Student(Person):
#     def __init__(self, name, age,coure):
        
#         super().__init__(name, age)
#         self.course = coure


#     def show_course(self):
#         print(self.course)






# student = Student('raju',34, 'science')
# # print(student.name, student.age, student.show_course(),)
# Student.display()





#*************************************************
# *************ABSTRACT METHOD

# from abc import ABC,abstractmethod

# class bank(ABC):

#     @abstractmethod
#     def deposite(self):
#        pass

#     abstractmethod
#     def loan(self):
#         pass

# class SBI(bank):

#     def deposite(self):
#         print("deposite is exicuted")

#     def loan(self):
#         print("loan is applied")


#     def profit(self):
#         print("profit")

# sbi = SBI()
# sbi.profit()
# sbi.deposite()
# sbi.loan()

#****************************************************************************************************************


#*****************task*******************************************************************************************
#****************************************************************************************************************


from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area():
        pass

# child class rectangle
class Rectangle(Shape):

    def __init__(self,lenth,width,):
        self.lenth = lenth
        self.width = width

    def area(self):
        rect_area = self.lenth * self.width
        print(rect_area)
        

# child class circle
class Circle(Shape):
    
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        circ_area= 3.14 * self.radius * self.radius
        print(circ_area)
    
rect = Rectangle(10,5)
rect.area()
circ= Circle(7)
circ.area()


    





