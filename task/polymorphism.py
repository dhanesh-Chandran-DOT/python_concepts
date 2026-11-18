#************************************************************************************************


#*******polimorphism**************************************************

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"hi i am peron {self.name},my age is {self.age}")


class Employee(Person):
    def __init__(self, name, age,emp_id,salary,job_roll):
        super().__init__(name,age)
        self.emp_id = emp_id
        self.salary = salary
        self.job_roll = job_roll

    def display(self):
        print(f"hi i am employee{self.name},my age is{self.age},my id is{self.emp_id},my salary is {self.salary},my job roll is{self.job_roll}")


class Father(Person):
    def __init__(self, name, age,no_of_children):
        super().__init__(age,name)
        self.no_of_children = no_of_children

    def desplay(self):
        print(f"hi i am father{self.name}my age is{self.age},no of children i have is{self.no_of_children}")

class Son(Person):
    def __init__(self, name, age,father_name):
        super().__init__(name,age)
        self.father_name = father_name

    def display(self):
        print(f"hi i am son {self.name},my age is{self.age},my father name is(self.father_name")

class Husbent(Person):
    def __init__(self, name, age,wife_name, date_of_marrage):
        super().__init__(name, age)
        self.wife_name = wife_name
        self.date_of_marrage = date_of_marrage


    def display(self):
        print(f"hi i am Husbent{self.name}, my age is{self.age},marrage date is{self.date_of_marrage}")



person = Person("krish",40)
person.display()

emp = Employee("raji",22,2999,30000,"HR")
emp.display()


father = Father("krish",40,4)
father.display()

son = Son("theju",18,"krish")
son.display()

husbent = Husbent("krish",40,"jaya","12/3/25")
husbent.display()





#**************************************************************************

#***********OOPS PROJECTS**************************************************



from abc import ABC, abstractmethod
class Bank_account(ABC):
    @abstractmethod
    def calculate_interest__init__(self):
        pass
    def __init__(self,account_holder,_account_type,__balance):
        self.account_holder = account_holder
        self.account_type = _account_type
        self.balance = __balance

    @property
    def balance(self):
        return self.__balance

#  @bank_bal.setter
#     def bank_bal(self,deposit_amt):
#         if deposit_amt <= 0:
#             raise "deposite amount cannot be zero or a negative value"
#         self.__bank_bal = self.__bank_bal + deposit_amt

    @balance.setter
    def balace(self,__balance):
        if __balance  <= 0:
            raise "balance cannot be zero or negative value"
        self.__balance = self.__balance + __balance


class Savings_Account(Bank_account):
    def __init__(self, account_holder, _account_type, __balance):
        super().__init__(account_holder, _account_type, __balance)

    def calculate_interest__init__(self):
        return self.balance * 0.05



    #child2

    class CurrentAccount(Bank_account):

        def __init__(self, account_holder, _account_type, __balance):
                super().__init__(account_holder, _account_type, __balance)



        



         
    


