#***********************************************
#******task6************************


file_path = 'C:/Users/dhaneshkr/Desktop/friends.txt'
#1

def read_filename():
    try:
        with open(file_path,'r') as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print("file not found - friends.txt illa")


read_filename()

#2
def creat_file():
    try:
        with open(file_path,'w')as file_1:
            data_1 = file_1.write('hello i am dhanesh\n')
    except Exception as e:   
        print('Error found :',e) 

creat_file()

#3

def name_file():
    try:
        friend_name = input('enter your friend name:')
        with open(file_path,'a') as file_3:
            file_3.write(friend_name)
    except Exception as e:
        print(f'Error found {e}')

name_file()



