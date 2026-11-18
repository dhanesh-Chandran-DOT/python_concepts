#************************************************************
#******set_dist*********************************************

#1

# fruit_list = {'apple','banana','orange','mango','grapes'}
# print(fruit_list)
# print(len(fruit_list))


# #2

# numbers = {10, 20, 10, 30, 20, 40, 50, 30}
# print(numbers)


#3

# colors = {"red","blue","green"}
# colors.add("yellow")
# colors.add("black")
# print(colors)

# colors.remove("blue")
# print(colors)


#4

# student1 = {"Python", "Java", "SQL", "HTML"} 
# student2 = {"Python", "C++", "SQL", "CSS"}
# print(student1.intersection(student2))


# #5

# student1 = {"Python", "Java", "SQL", "HTML"} 
# student2 = {"Python", "C++", "SQL", "CSS"}
# print(student1.union(student2))

# print(student1)                 # {'SQL','HTML','Python','Java'}

# print(student2)                 # {'c++','SQL','CSS','Python'}



# #6

# student = {'name':'rahul','age':'20','course':'python','city':'kochi'}
# print('whole dictionary',student)
# print('keys are',student)
# print(student['name'])
# print(student['age'])
# print(student['course'])



# #7
# employee = {    "name": "Anu",   "age": 25,      "salary" : 25000}
# employee.update({"department":"IT"})    # For adding "department":"IT" to the list
# print(employee)
# employee.update({"salary":"30000"})
# print(employee)
# employee.update({"age":"26"})
# print(employee)


#8

# marks = {    "Maths": 80,   "Computer": 85,  "Science": 75, "english":90}
# print(marks.keys())
# total_mark = marks["Maths"] +   marks["Computer"]   +   marks["english"]    +   marks["Science"]
# print(total_mark)
# print(len(marks))
# print(total_mark / len(marks))           #   to find the avrage marks

#9


# student = {"name": "Arun",  "age": 21,  "marks": 85,   "course": "python" ,   "age": 21,   } 
# print(student["name"])
# print(student["course"])
# if(student["marks"]>50):
#     print("the student is passed")
# else:
#     print("student failed")
# student.update({"grade":"A"})
# print(student)



#10

morning_batch = {"Anu", "Rahul", "Arun", "Meera"} 
evening_batch = {"Rahul", "Meera", "John", "Priya"}
print(morning_batch.union(evening_batch))
print(morning_batch.intersection(evening_batch))
print(morning_batch)
print(evening_batch)







