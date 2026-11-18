# list and tuple


#1
#*********************************

# student_list = ['reji','manu','sunil','vishnu','abhinav']
# new_student1 = input('enter student name')
# student_list.append(new_student1)
# print(new_student1)


#2
# #*********************************
# list1 = ["rice","suger","milk"]
# list2 = ["bread","eggs","butter"]
# list1.extend(list2)
# print(list1)
# print('total number of items is',len(list1) )

#3
# #***********************************
# numbers = [10,20,10,30,40,10,20,50]
# num1 = int(input('enter a number'))
# print(numbers.count(num1))

#4
# #*************************************
# list3 = [1,2,3,4,5,6,7,8,9,10]
# print(list3)
# list3.reverse()
# print(list3)

#5
# #***************************************
# list4 = [78,45,92,56,88,34,67]
# print(list4)
# list4.sort()
# print(list4)

#6
# #****************************************
# list5 = ["apple","banan","mango","orange"]
# fruit_name = input('enter the fruit_name:')
# fruit_name1 = int(input('enter the possition of the fruit:'))
# list5.insert(fruit_name1,fruit_name)
# print(list5)

#7
# #*******************************************
# subjects = ["English", "Maths", "Science", "Computer", "History"]
# print(subjects)
# removed=subjects.pop()
# print(subjects)
# print(removed)

#8
#**********************************************

# colours = ["red", "blue", "green", "yellow", "blue"]
# user = input('enter a colour to remove:')
# colours.remove(user)
# print(colours)

 #9
 #  #********************************************
# list6 = ["html","c++","python","php","java"]
# print(list6)
# list6.clear()
# print(list6)
# if(list6==True):
#     print('enter list is not empty')
# else:
#     print('list is empty')

#10
#**************************************************
students = ["Anu", "Rahul", "Meera", "Arun", "Diya"]
students.append("kiran")
print(students)
list2 = ['sneha','vijay']
students.extend(list2)
print(students)
students.insert(2,'ravi')
print(students)
print(students.count("Anu"))
students.sort()
print(students)
students.remove("Rahul")
print(students)
students.pop()
print(students)
students.reverse()
print("fanal list is :",students)







