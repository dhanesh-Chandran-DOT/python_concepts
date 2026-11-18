# #*********************************************************
# #*********FUNCTION TO ADD TWO NUMBERS ****************************************

# def display_sum(num1,num2):  # function name
#     sum = num1 + num2        # body
#     #print(sum)
#     print('the sum of ',num1,'and',num2,'is',sum)



# # a function will have
# #1. function name
# #2.input()
# #3. body of the function
# #4. output


# # display_sum(2,5)
# # while we define input variable in the function definition , we are 
# #creating new variable with scope with in the function


# # # call the function /invoking the function
# # display_sum(8,7)        #the sum of  8 and 7 is 15
# # display_sum(2026,8)
# # display_sum(9.8,6,)  
# # display_sum('happy','diwali')
# # display_sum(8,True)    #bool is 1 so sum is 8 + 1 = 9

# def display_sum_customer():
#     # print('we will display the sum of 2 numbers you enterd')
#     # num1 = float(input('enter the first number:'))
#     # num2 = float(input('enter the second number:'))
#     # sum = num1 + num2
#     # print('the sum of' ,num1,'and',num2,'is',sum)
    


# #display_sum_customer()


# def display_name():
#     name1 = input('enter your name ')
#     print("hi", name1 ,'good after noon')

# display_name()              #enter your name dhanesh
#                             #   hi dhanesh good after noon


# # Generating a multiplication table
# num = 5
# print('multiplication table of',num)
# print('*********************************')
# for i in range(1,11):
#     print(i,'x',num, '=', i*num)
# print('*********************************')


# function to display multiplication table of the  number

# def display_multiplication_table():
#     print('we will display the multiplication table of the number you enter')
#     num = int(input('enter the number:'))
#     print('******************************')
#     print('multiplication table of', num)
#     print('______________________')
#     for i in range(1,11):
#         print(i,'x',num, '=',(i*num))
#     print('**************************')

# display_multiplication_table()



# task***************************
#input 5 score
#calculate the sum
#calculate the avg
#calculate the largest
#calculate the smallest

# subjects = [46,78,98,37,55]

# def sub_score():
#     total=sum_score ()
#     print("Total:",total)
#     largest_score()
#     smallest_score()
#     avarage(total)



# def sum_score ():
#     total_mark = 0
#     for i in subjects:
#         total_mark = total_mark + i
#         #i=i+1
#     return total_mark

# def  avarage(total):
#         avarage1 = total / len(subjects)
#         print(avarage1)

    
# def largest_score():
#     lager1 = max(subjects)

#     print(lager1)

# def smallest_score():
#     smaller1 = min(subjects)
#     print(smaller1)



# sub_score()


#*******************************************************************************************
#**************** OPTIONAL ARGUMENTS 
#***************** EXPONENT********************************


# def calculate_exponent(num,exp = 2):                    #     arguments
#     print(num** exp)
# calculate_exponent(5)
# calculate_exponent(5,3)                                 #      5*5*5 = 125

# def create_wish(name,wish = 'good day'):
#     print(f'hi{name},{wish}')

# create_wish('anjay')                                    #hianjay,good day                                                       
# create_wish('anjaly','mrng')                            #hianjaly,mrng
# # we can give values of arguments explicity
# create_wish(wish = 'good afternoon',name = 'anjaly')
# # we can give values of arguments explicity.



# # task


# #1

# def calculate_result():
    
#     python = 67
#     mathematics = 45
#     science = 98
#     marks = python + mathematics + science
#     return marks
# marks1 = calculate_result()
# print('total mark is:',marks1)

# def calculate_avg():
#     avarage = marks1 / 3
#     return avarage
# avg = calculate_avg()
# print('avarage mark is:',avg)

# def highest_mark(python,mathematics,science):
#     highest_mark1 = max(python ,mathematics ,science)
#     print(f'highest mark is :{highest_mark1}')
#     return highest_mark
# p = float(input('enter the python mark:'))
# m = float(input('enter the mathematics mark:'))
# s = float(input('enter the science mark:'))

#highest_mark(p,m,s)


#**************************************************************************
#**************************************************************************

# def devide(num,den):
#     result = num / den
#     print(f'the answer is: {result}')

# devide('a','b') #type error
# devide(40,10)
# devide(80,4)
# devide(40,0)    #zero devition error

# exeptional handing
# we write specific criteria so that code flow is not inturrupted.
# we write potential runtime making code inside ' try' block
# and the exeption will be caught by the 'except' block 


# def devide_new(num,den):
#     try:
#         result = num / den
#         print(f'the answer is: {result}')
#     except:
#         print('there is a problem')

# devide_new('a', 'b') #type error
# devide_new(40,10)
# devide_new(80,4)
# devide_new(40,5)

#rewriting the function with exception block displaying the appropriate error message

def devide_new1(num,den):
    try:
        result = num / den
        print(f'the answer is: {result}')
    except  Exception as e:
        print(f'there is a problem:{ e}')

print('the end')

devide_new1('a', 'b') #type error
devide_new1(40,10)
devide_new1(80,4)
devide_new1(40,0)

#new_2


def devide_new2(num,den):
    try:
        result = num / den
        print(f'the answer is: {result}')
    except  TypeError:
        print('pleas make sure you are entering numbers')
    except ZeroDivisionError: 
        print('please make sure give a non zero value as dinominator')
    except Exception as e :
        print(f'there is a problem :{e}')
        print('the end')

        
devide_new2('a', 'b') #type error
devide_new2(40,10)
devide_new2(80,4)
devide_new2(40,0)




