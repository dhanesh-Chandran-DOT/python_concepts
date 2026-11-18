string1 = 'dhanesh'

string2 = 'python'
string3 = 'programming'

print(string1)
print(string2)
print(string3)
print('\n')
print(string2,string3)

# by default python prints a new line at the end.

# changing the end string from '\n' to '&'

print(string1, end='& ')    #dhanesh&
print(string2, end='& ')    #python&
print(string3, end='& ' )   #programming
print('\n', end='& ' )      #new line
print(string2,string3, end='& ')        #python programing&


s1 = 'ICT'
s2 = 'Academy'
s3 = 'of'
s4 = 'kerala'

# String concatenation

print(s1 + s2 + s3 + s4)
print(s1, s2,s3,s4)

combined_string = s1 + ' ' + s2 + ' ' + s3 + ' '+ s4
print( combined_string)


print(s1)
print(s1 + s1 + s1 + s1 + s1)
print(s1*5)
print(( s1 + ' ') * 5)
print((s1 + '\t') * 5)
print((s1 + '\n') * 5)

#print(*********************index******************)

print(string3)
print(string3[0])
print(string3 [5])      #print caracter value at 5th index
     # we cannot go beyond the maximum index of a string.

string1 = 'hueyitguv2 hkjdqwsuijknwquljhywn'
print(string1 [-2]) 






print(s1 + s2 + s3 + s4)
print(s1, s2,s3,s4) 

s1 = 'ICT'
s2 = 'Academy'
s3 = 'of'
s4 = 'kerala'

print(s1)
print (s2)
print(s3)
print(s4)

print( s1, s2,s3,s4)

s1 = 'trivandrum'
print(s1[-3])
print(s1[6])
print(s1[0:5]) #triva
print(s1[6:10]) #drum
print(s1[4:7]) #and


print(s1[:5]) # start index till 5.               'triva'
print(s1[6:]) # from 6th index till last index   'drum'


print(s1[0:5:2])
print(s1[:5:2])

#  start, end, step

string_demo = "join our office programs in kerala's IT park"
s1 = 'elephant'
print(string_demo[5::1])
print(string_demo[5::2])

# reversing a string

print(s1[::-1])
print( string_demo[::-1])


#*********************************
# function********************

s1 = 'triVANDrum'
print(s1)
print(s1.lower()) # convert string to lowercase 'trivandrum 
print(s1.upper()) # convert strint to uppercase 'TRIVANDRUM'
print(s1.swapcase()) # Convert sting lower to upper and to lower 'TRIvandRUM
print(s1.capitalize()) # Capitilize first charector of the sting in capital.