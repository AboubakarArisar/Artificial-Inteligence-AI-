#some string methods and practice of string

#string it self is an array of characters

str = "Aboubakar"
length = len(str)
print(length) #length of the string

print(str[0]) #first character of the string
print(str[length-1]) #last character of the string

# string methods

print('Ab' in str) #checking if the substring is in the string or not

print(str.upper()) #converting the string to upper case
print(str.lower()) #converting the string to lower case


# slicing 
print(str[0:4]) #slicing the string from 0 to 4 while 4 is not included
print(str[4:]) #slicing the string from 0 to 4



#                 Exercise 2

# • S= “ This is a university “
# • Find the length of string
# • Replace university by college
# • Convert lower case into upper case
# • Display 2nd last character
# • Return the string without any whitespace at the beginning or the end.
# • Find the number of words in variable S

s = "This is a university"
length = len(s)
print(length) #length of the string

s = s.replace('university', 'college')

print(s) #replacing university with college

print(s.upper()) #converting the string to upper case

print(s[-2]) #displaying the 2nd last character

print(s.strip()) #returning the string without any whitespace at the beginning or the end

print(len(s.split())) #finding the number of words in the string