#**********TASK 6**********************************

# #1

# def calculate_grade():
#     marks = int(input('enter the mark:'))

#     if(marks >= 90):
#         #print('grade A')
#         return 'A'
#     elif(marks >= 75):
#         #print('grade B')
#         return 'B'
#     elif(marks >= 60):
#         #print('grade c')
#         return 'C'
#     elif(marks >= 40):
#         #print('grade C')
#         return 'D'
#     else:
#         #print('Stent is fail')
#         return 'fail'
# grade=calculate_grade()
# print(grade)



#2

# def calculator():
#     first_num =int(input('enter the first number:'))
#     second_num =int(input('enter the second number:'))
#     operator = input('oparator is:')
#     if operator == '+':
#         operation = first_num + second_num
#         return operation
#     elif operator == '-':
#         operation = first_num - second_num
#         return operation
#     elif operator == '*':
#         operation = first_num * second_num
#         return operation
#     elif operator == '/':
#         operation = first_num / second_num
#         return operation
# operation_done = calculator()
# print(operation_done)

#3

# def simple_interest():
#     principal = (int(input('enter the principal:')))
#     rate = float(input('enter the rate:'))
#     time = float (input('enter the time:'))
#     interest = principal * rate * time /100
#     return interest 
# simple_interest1 = simple_interest()
# print(simple_interest1)

#4

# def last_character(apple):
#     string =apple [-1]
#     return string
# print('The last charecter of the string is:',last_character('apple'))

# #5

# def calculate_bill(units):
    
#     if(units >= 100):
#         print((units)*5 )
#     elif(units <= 200):
#         print((100*5) + (100)*7)

#     else:
        
#         print((100)*5 + (100)*7 + (units)*10)
#     return units
# units =int( input('unit of electricity consumed:'))
# calculate_bill(units)


       
#6

def count_even(list):
    count = 0
    for i in list:

        if(i % 2 == 0):
            count = count + 1
    return count
list = [12,14,9,74,11,51]
count_1=count_even(list)
print(f"count is : {count_1}")
        



