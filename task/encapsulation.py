#*******************************************************************

#*********encapsulation********************************************




# class Bankaccount:
#     def  __init__(self,owner_name,bank_bal,account_type):
#         self.owner_nanme = owner_name
#         self.__bank_bal = bank_bal
#         self._account_type = account_type

# # to get the private attribute

#     @property
#     def bank_bal(self):
#         return self.__bank_bal                                          # '__' is given so there is no need to give underscore' __' to print

#     @property
#     def account_type(self):
#         return self._account_type


#     # update private attribute

#     @bank_bal.setter
#     def bank_bal(self,deposit_amt):
#         if deposit_amt <= 0:
#             raise "deposite amount cannot be zero or a negative value"
#         self.__bank_bal = self.__bank_bal + deposit_amt
        
#     @account_type.setter
#     def account_type(self,ac_type):
#         if ac_type == '':
#             raise "account type is valide"
#         self.account_type = ac_type

# bank = Bankaccount("ABC",12000,"Savings")


# bank.bank_bal
# print(bank.account_type)


# bank.__bank_bal = 123
# print(bank.bank_bal)
# print(bank.account_type)                                                




#****************************************************************************************

#******task*****************************************************************************



# class Employee:
#     def __init__(self,employee_name,department,salary):
#         self.employee_name = employee_name
#         self._department = department
#         self.__salary = salary


#     @property
#     def salary(self):
#         return self.salary

#     @salary.setter
#     def salary(self,salary):
#         if salary <= 0 :
#             print( "salary cannot be negative")
#         self.__salary = salary


# class Manager(Employee):
#     def display_details(self):
#         print("employee_name:",self.employee_name)
#         print("department:",self._department)

# #****object creation
# # 
       
# mg = Manager("dhanesh","software",25000)
# mg.salary = 50000
# mg.display_details()
# print("salary",mg.salary)
# mg.salary = 123
# print("update",mg.salary)

 


        
# # vehicle task

class vehicle:
    def __init__(self,vehicle_name,_rental_type,rental_price):
        self.vehicle_name = vehicle_name
        self._rental_type = _rental_type
        self.__rental_price = rental_price
    @property
    def rental_price(self):
        return self.__rental_price
    
    @rental_price.setter
    def rental_price(self,value):
        if value <= 0:
            raise ValueError("rental cannot be negative")
        
        self.__rental_price = value

        @property
        def _rental_type(self):
            return self._rental_type

        def display_details(self):
            print("Vehicle Name:" ,self.vehicle_name)
            print("Rental Type:" ,self._rental_type)
            print("Rental Price: ",self.__rental_price)



# PART B*******************************************************




class Car(vehicle):


    def calculate_rent(self,days):
        return self.rental_price*days

    def display_details(self):
        print("vehicle name",self.vehicle_name)
        print("rental type",self._rental_type)
        print("__rental_price",self.rental_price)




class Bike (vehicle):
    def calculate_rent(self,days):
        return self.rental_price*days

    def display_details(self):
        print("vehicle name",self.vehicle_name)
        print("rental type",self._rental_type)
        print("__rental_price",self.rental_price)
    


v = Car("punch",",monthly",100000)
print(v.calculate_rent(30))
v.display_details()








