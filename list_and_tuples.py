# list is a data type to store the collection of values
#since it is a combination of other data type (int, float,)
#sring,bool)we call it as dirrived datatypes






# #declare a list
# name = ""
# print(type(name))

# #method1
# list_name1 = []
# print(type(list_name1))

# #method2

# list_name2 = ('dahnesh','raju','renu')
# print(type(list_name2))


# #method3

# list_name3 = list()
# print(type(list_name3))

# #fetching values using index from a list
# list_name2 =['raju','renu', 'dhanesh']
# print(list_name2[0])
# print(list_name2[1])
# print(list_name2[2])
    


# # list containing multiple datatypes

# #   personal info as a list : name , age, graduation year , university, height


# amar_info = ['amar' , 22 , 'CUSAT' ,177.5 ,list_name2]
# print(type[amar_info])

# print(amar_info[0])
# print(amar_info[1])
# print(amar_info[2])
# print(amar_info[3])
# print(amar_info[4])





#progm

list1 = [1,2,3]
list2 = [True,False,True]
print(list1 + list2)


#list Functions**********************

list1 = [1,7,3]
list2 = [True,False,True]
list_name2 =['raju','renu', 'dhanesh']

print(list1)
list1.sort
print(list1)

print(list_name2)       #unsorted
list_name2.sort()       #sorting is done here
print(list_name2)       #sorted

list1.sort(reverse= True)       #sort the other way (desending order)
print(list1)  


# 1st_names2 = ['raju','renu', 'dhanesh',7,3,1]

list_name2.extend(list1)            #extended the values of the list
print(list_name2)

list2.append(list1)             #list1 was added as the last value of list2
print(list2)           


list1.append('A')
print(list1)                    # [7,3,1,A]

list1.reverse()                 #[A,1,3,7]
print(list1)


print('the no of times true appear in the list =',list2.count(True))
print('the no of times false appear in the list =',list2.count(False))
print("the no of times 'x' appear in the list =", list2.count('x'))             #ckeck the count of value 'true



# value at the last index
print(list2[-1])

#Fetching no of items in the list
len(list2)
print('total no of elements',list2,'is',len(list2))

# value at the last index

print(list2[1])
print(list2[len(list2)-1])


print('before clear')
print(list2)

list2.clear()                       #clear all value list2

print('after clear')
print(list2)


print('****************************************************************************************************')
print('before inserting any value',list1)


# in order to do [7,3,2,'A'] -> [7,3,100,1,'A']
#is inserting 100 at index 2
list1.insert(2,100)
print('after inserting a value', list1)

print('before removing 3', list1) 
list1.remove(3)
print('after removing 3',list1) #[7,100,1,A]


print('************************************************************************************************')


list1.pop()     #Eleminate the element
print(list1)



tuple1 = [1,2,3]


tuple2 = (2026,'nov',3.75,[8,9,True])
tuple3 =tuple()
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

print(tuple2[2])                    #we can fetch value using index

print(tuple2.count('nov'))
print(tuple2.index('nov'))

# once a tuple created, we cannot make any changes to it.

# list -> mutable               (can change to values)
# tuple -> immutable            (cannot make change to values)

del(tuple2)
del(list2)


#print(tuple2)               #get an error saying that variable
#print(list2)
