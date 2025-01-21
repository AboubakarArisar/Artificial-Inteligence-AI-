#Type Conversion in Python refers to the conversion of one data type into another data type.

#There are two types of Type Conversion in Python:

#Implicit Type Conversion
#Explicit Type Conversion


#Implicit Type Conversion : python automatically converts without user involvement 
#Explicit Type Conversion : user involvement is needed to convert from one data type to another data type

#Implicit Type Conversion


integerVariable = 10
floatVariable = 10.5

sum = integerVariable + floatVariable
print(sum)

#Explicit Type Conversion


integerVariable = 10
floatVariable = 10.5

sum = integerVariable + int(floatVariable)
print(sum)


#in easy words we can say that in implicit conversion we want to convert small data type to large data type while in explicit we do convert larger data type to samller one 