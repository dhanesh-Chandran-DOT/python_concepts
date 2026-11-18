#********************************************************************************************************************************

#********Employeee salary management system***************************************************

# #Develop a simple Employee Salary Management System using Python OOP concepts. 
# 1. Create an abstract class named Employee. 
# ○ Include an abstract method named calculate_salary(). 
# ○ Include a method named display_details(). 
# 2. Encapsulate the employee's basic salary using a private attribute. 
# ○ Provide a method to retrieve the basic salary. 
# 3. Create two child classes: 
# ○ PermanentEmployee 
# ○ ContractEmployee 
# 4. Implement calculate_salary() differently: 
# ○ Permanent Employee: Basic Salary + 20% allowance. 
# ○ Contract Employee: Basic Salary + 5% allowance. 
# 5. Create objects of both employee types and demonstrate: 
# ○ Displaying employee details. 
# ○ Calculating and displaying their salarie
# 
 

from abc import ABC,abstractmethod

class Employee(ABC):

    def __init__(self,name,age,emp_id,emp_roll,salary):
            self.name = name
            self.age = age
            self.emp_id = emp_id
            self.emp_roll = emp_roll
            self.__salary = salary

        

    @abstractmethod
    def calculate_salary(self):
         self.__salary = salary

    def display_details(self):
        print("employee name:",self.name)
        print("age is:",self.age)
        print("employee id:",self.emp_id)
        print("employee roll:",self.emp_roll)
        print("employee salary:",self.__salary)



class PermanentEmployee(Employee):
    def calculate_salary(self):
         return self.calculate_salary()*20/100

class contractEmployee(Employee):
    def calculate_salary(self):
         return self.calculate_salary()*5/100



E1 =   PermanentEmployee("aji",28,123,"hr",50000)
E2 =   contractEmployee("Raju",26,456,"manager",100000)

E1.display_details()
E2.display_details()


#2 

# #
#           Vehicle Rental Management
# 
#   
# Develop a simple Vehicle Rental Management System using Python OOP concepts. 
# 1. Create an abstract class named Vehicle. 
# ○ Include an abstract method named calculate_rent(days). 
# ○ Include a method named display_vehicle_details(). 
# 2. Encapsulate the rental price per day using a private attribute. 
# ○ Provide a method to retrieve the rental price. 
# 3. Create two child classes: 
# ○ Car 
# ○ Bike 
# 4. Implement calculate_rent(days) differently: 
# ○ Car: Rental price per day × number of days + ₹500 service charge. 
# ○ Bike: Rental price per day × number of days + ₹100 service charge. 
# 5. Create objects of both vehicle types and demonstrate: 
# ○ Displaying vehicle details. 
# ○ Calculating rental charges for 3 days. 
# ○ Displaying the final rental amount.



from abc import ABC ,abstractmethod

class Vehicle(ABC):
    def __init__(self,name,vehicle_no,price):
          self.name = name
          self.vehicle_no = vehicle_no
          self.__price = price              #rental price


    @abstractmethod
    def calculate_rent(self):
            pass

    @property
    def rental_price(self):
         return self.__price
                  

    def display_details(self):
        print("name of the vehicle:",self.name)
        print("vehicle number is :",self.vehicle_no)
        print("price of the vehicle is :",self.rental_price)


class Car(Vehicle):
    def calculate_rent(self,days):
        rent = self.rental_price*days + 500
        print(rent)
    
         


class Bike(Vehicle):
    def calculate_rent(self,days):
         return self.rental_price*days + 100


c = Car("Punch",2400,10000)
b = Bike("MT",1200,9000)  

print("car rent for 3 days:", c.calculate_rent(3))     
c.calculate_rent(3)

print(" bike rent for 5 days:",b.calculate_rent(5))
b.calculate_rent(5)
c.display_details()
b.display_details()
          


