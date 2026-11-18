#************************************************************************************************************************
#******************checking whether a number is bigger than 50***********************************************************

#number = input('please enter the number:')
#number_int = int(number)
#if(number_int > 50):
 #   print('entered number is bigger than 50')
#if(number_int < 50):
#    print('entered number is less than 50') 
#else:
 #   print('the number entered is not bigger than 50')






# conditions and exoected output
# number > 50 # the entered is number biggrer than 50 print
# number < 50= # the number not bigger than 50 




#num = input('please enter the number:')
#num = float(num)
#if((num % 2)==0):
 #   print('it is an even number')
#else:
 #   print('it is an odd number')   



#*******************************************************************************************************************

#temp = float(input('Enter a number'))

# >=35 =  :very hot
# 25 - 35 :warm
# 15 - 25 :cold
# <=15 :freezing

#if(temp1 >= 35):
 #   print('very hot')
#else:
# if(temp1 >= 25):
#         print('warm day')
#     else:
#         if(temp1 >= 15):
#             print('cold day')
#         else:
#             print('freezing')        


# nested if else loop

# if(temp >= 35):
#     print('very hot')
# elif(temp >= 25):
#     print('warm day')
# elif(temp >= 15): 
#     print('cold day')
# else:
#     print('freezing')





#********************************************************************************************
#*********iterative statements***************************************************************
#**********for loop: use when no of iterations are known
#**********while loop:use when no of iteration is unknown and should know stoping poin or comdition

# # print your name 10 times

# for i in range (10): # we are giving  no of iteration
#     print(i,': dhanesh') # itrative

#     print('using step operator')

#     # rage(start,end,step) #if step is not mentioned means step = 1

#     for i in range (3,10,3): # we are giving  no of iteration
#         print(i , ' : dhanesh')


# # giving step as a negative value

# for i in range (10,3,-3): # start with 10 it jump 3 times forword like # 
#         print(i , ' : dhanesh')

#*****print all numbers <50***************************


# for i in range(1,50,2):
#     print(i,' :  odd number')

# # even number*************
# for i in range(21,50,2): # start with 21 2 step forword then we get # this is odd number from 21 - 49
#     print(i,' : this is odd number')


# #**** while loop *************************

# num = 1 
# while(num < 10):
#     print(num)
#     num = num + 1

# print('end of while loop')


# num = 1
# while(num < 50):
#     print(num)
#     num = num + 2
# print('end of number')



# print('odd numbers between 20 and 50') # odd numbers between 20 -50
# num1 = 21
# while(num1 < 50):
#     print(num1)
#     num1 = num1 + 2  


# print('\n','odd numbers between 20 and 50') #adding all the odd numbers in a line 
# num1 = 21
# while(num1 < 50):
#     print(num1, end =',')
#     num1 = num1 + 2







age = int(input('enter your age :'))
valid_id = input('do you have a valid id card (y/n):')

else:
valid_id = False


print('we are checking you eligeblity')
      
if(age >= 18):
    if(valid_id):
        print('you are eligible to vote')
    else:
        print('you are not eligible to vote')
        print('your need a valid_id card to be eligible')
else:
    print('you are not eligible to vote ')
    print('you should be 18 or above to be eligible')



    


# doing the same process using logical operator

if((age >= 18) and (valid_id)):
    print('you are eligible to vote')
else:
    print('you are not eligible to vote')
