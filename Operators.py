# *********************************************************
#*****Arithmatic*******************************************
# binary operators : we need min 2 operands.

num1 = 555
num2 = 10

sum = num1 + num2   # addition
difference = num1 - num2  #substraction
product = num1 * num2 # multiplication
division = num1 / num2 # division
exponent = num1 ** num2 #exponent
remainder = num1 % num2 # modulus
floor = num1 // num2 # division

print(num1,'+', num2, '=', sum)
print(num1, '-', num2, '=', difference)
print(num1, '*', num2, '=', product)
print(num1, '/', num2, '=', division)
print(num1, '**', num2, '=', exponent)
print(num1, '%', num2, '=', remainder)
print(num1, '//', num2, '=',floor)

# **************Relation*****************
#****************************************
print(num1, '>', num2, num1 > num2) #True
print(num1, '<', num2, num1 < num2) #False
print(num1, '>=', num2, num1 >= num2) #True
print(num1, '<=', num2, num1 <= num2) #False
print(num1, "==", num2, num1 == num2) #False
print(num1, '!=', num2, num1 != num2) #True

#********************************************
#**********Logical operators****************

# AND - All has to be in agreement
# OR - At least 1 must be agreement
# NOT - Opposite

statement_1 = True
statement_2 = False
statement_3 = True
statement_4 = False

#AND

print( statement_1 and statement_2) #True and False = False
print( statement_1 and statement_3) #True and True = True
print(statement_2 and statement_4) #True and False = False

#OR

print( statement_1 and statement_2) #True and False = True
print(statement_1 and statement_3) #True and True = True
print( statement_2 and statement_4) #False and False = False

#NOT

print(not statement_1) # not True = False
print(not statement_2)#not False = True