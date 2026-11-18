#*************************************************************************************************************
#****************************SET******************************************************************************
# heterogenous data type
# cannot acces data using index
# duplicates are not allowed
# mutable

#declaring a set


#method 1
# #**************************************
# set1 = {}                                       # it is not a set but it is a dictionary

# #method 2
# #**************************************
# set2 = {12,55,88,'88',2026,'bsnl',True,88}                               # this is a set

# #method3
# #***************************************
# set3 = set()


# print(type(set1))
# print(type(set2))
# print(type(set3))

# print(set2)  


# # it accept all data types becoz it is heterogous
# # duplicate values are deleted



# roll = {1,2,3,4,5,6}
# roll_odd = {1,3,5}
# roll_even ={2,4,6}


# random = {1,5,9,4}

# random.add(2026)
# print(random)

# print(random.difference(roll_odd))
# print(roll_odd.difference(random))

# print(roll.issuperset(roll_odd))
# print(roll.issubset(roll_odd))
# print(roll.issuperset(random))

# print(random.intersection(roll_even))
# random.remove(9)
# print(random)

# copy = random.copy()
# print(copy)




#****************************************************************
#***************DICTIONARY***************************************



# diclaring a dictionary

# method1

dict1 = {}

# method2

dict2 = {'key1': 'value1','key2':'value2',8:2026,True: 'yes it is a word'}

dict3 = dict()

print(type(dict1))
print(type(dict2))
print(type(dict3))


print(dict2)


sample_dist = {1:'one',0:'zero',1:'True',1:'ICT'}
print(sample_dist)

# {1:'ICT',0:'zero}  becoz ict is the leterst value
# duplication keys are not allowed.


print(dict2['key2'])


student_dist = {'name':'dhanesh',
                'age':'22',
                'university':'calicut',
            'district':'palakkad'}

print('whole dictionary ',student_dist)

print('key are ')
print(student_dist.keys())


print('values are')
print(student_dist.values())

print('items are')
print(student_dist.items())


student_dist ['university'] = 'calicut university'
print(student_dist)



personal_info = {'name':'dhanesh','age':'26','district':'palakkad','qaulification':'MSc'}

print('whole information',personal_info)

print(personal_info)













