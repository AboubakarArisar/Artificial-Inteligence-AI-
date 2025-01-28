#printing hello world
# print("Hello, world")

#python variables
# x = 5
# y = 'hello world'

# print(x, y)


#                           Excersice 1 in lab 1 
# • Create a variable named carname and assign the value Audi to it.
# • Create a variable named x and assign the value 30 to it.
# • Display the sum of 5 and 15, using two variables
# • Create a variable called z, assign x + y to it, and display the result.
# • Remove the illegal characters in the variable name:
# • 2my-first_name = "John“
# • Assign the same value to three variables in one code line.
# • Define same name to local and global variable and display its different values


carname = 'Audi' #carname variable having car value Audi
x = 30 #x variable having value 30

a = 5 
b = 15
print(a + b) #sum of 5 and 15 using two variables

z = a + b
print(z) #sum of a and b using a third variable z

# 2my-first_name = "Aboubakar #illegal variable name
my_first_name = "Aboubakar" #correct variable name

d = e = f = 10 #assigning the same value to three variables in one code line

def my_function():
    global x
    x = 25
    print(x)

my_function()
print(x)


