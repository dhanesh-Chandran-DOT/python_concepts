#*****************************************************************************************************
#*********************STUDENT INFORMATION*************************************************************

#1
#******************************************

student_name = ('raju')
age = (25)
height = (67.1)
currently_enrolled = True
subject_enrolled = ['english','hindi']
date_of_birth = (7,2,2000)
skill_known = {'css','python','excel'}
student_details = {'name':'raju','age':'25','height':'67','course':'python'}
course =student_details['course']
print(student_name,type(student_name))
print(age,type(age))
print(height,type(height))
print(currently_enrolled,type(currently_enrolled))
print(subject_enrolled,type(subject_enrolled))
print(date_of_birth,type(date_of_birth))
print(student_details,type(student_details))



#2
#*************************

python = 68
mathematics = 50
science = 76

marks = python + mathematics + science
print(marks)

average_mark= marks / 3
print(average_mark)

print("highest_mark",max(python,mathematics,science))
print("lowest_mark",min(python,mathematics,science))

if(python >= 40):
    print("student is passeed")
elif(mathematics >= 40):
    print("student is passed")
elif(science >= 40):
    print("student is passed")

else:
    print("student failed")



#3
#***************************
# marks = int(input('enter the mark'))

if(marks>= 90):
    print("grade A")
    grade = "A"
elif(marks >=75):
    print("grade B")
    grade = "B"
elif(marks >= 60):
    print("grade c")
    grade = "C"
elif(marks >= 40):
    print("grade D")
    grade = "D"
else:
    print("student failed")
    grade = "F"


if(python >= 40 and mathematics >= 40 and science >= 40):
    if(average_mark>=60):    
        print("student is eligible for the certificate",)
        certificate = 'eligible'     
    else:
        print("student is not elilgible for the certificate")
        certificate = 'not eligible'
        

else:
    print("failed")
    certificate = 'not eligible'

#4
#*********************************

sub_mark = [59,30,57,98,33]
print('sub_marks')
total_marks = 59 + 30 + 57 + 98 + 33
print(total_marks)
count = 0
count1 = 0
i = 0
for i in range(len(sub_mark)):
    if sub_mark [i] >= 40:
        count = count + 1
    else:
        count1 = count1 +  1
        print("student scored above 40 are:",count)
        print("student scored below 40 are:",count1)

#5
#************************************
     

i=1
while(i <= 50):
    print(i)
    i = i + 1

even_num = 0
even_sum = 0
while(even_num <= 50):
    if even_num % 2 == 0:
       print(even_num)
       even_sum = even_sum + even_num
       even_num = even_num + 1
    else:
        even_num = even_num + 1
print(even_sum)

odd_num = 0
odd_sum = 0
while(odd_num <= 50):
    if odd_num % 2 != 0:
       print(odd_num)
       odd_sum = odd_sum + odd_num
       odd_num = odd_num + 1
    else:
        odd_num = odd_num + 1
print(odd_sum)

#6

skills = { 'excel','python','java','sql','HTML'}
skills.add('php')
skills.remove('sql')
if 'python' in skills:
    print("student knows python ")
else:
    print("student does not know python")

print(skills)


#7

dict = {"student_name":student_name,"age":'age',"course":course,"totamark":total_marks,"average marks":average_mark,"grade":grade,"certificate eligibility ": certificate}
print(dict)


       
    







