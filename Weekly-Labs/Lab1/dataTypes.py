#There are some Builtin Data Types in Python

#. Text Type:	str

stringVariable = 'String Variable'
print(stringVariable)
print(type(stringVariable))

#. Numeric Types:	int, float, complex
intVariable = 1
print(intVariable)
print(type(intVariable))

floatVariable = 1.0
print(floatVariable)
print(type(floatVariable))

complexVariable = 1j
print(complexVariable)
print(type(complexVariable))


#. Sequence Types:	list, tuple, range

listVariable = ['apple', 'banana', 'cherry']  #list is mutable and ordered collection of items
print(listVariable)
print(type(listVariable))

tupleVariable = ('apple', 'banana', 'cherry') #tuple is immutable we can't change the values and ordered collection of items 
print(tupleVariable)
print(type(tupleVariable))

rangeVariable = range(6) #range is immutable and ordered collection of items
print(rangeVariable)
print(type(rangeVariable))

#. Mapping Type:	dict
dictVariable = {'name':'Aboubakar', 'age': 20} #dictionary is mutable and unordered collection of items
print(dictVariable)
print(type(dictVariable))

#. Set Types:	set, frozenset
setVariable = {'apple', 'banana', 'cherry'} #set is mutable and unordered collection of items
print(setVariable)
print(type(setVariable))

frozensetVariable = frozenset({'apple', 'banana', 'cherry'}) #frozenset is immutable and unordered collection of items
print(frozensetVariable)
print(type(frozensetVariable))

#. Boolean Type:	bool
boolVariable = True
print(boolVariable)
print(type(boolVariable))

#. Binary Types:	bytes, bytearray, memoryview
bytesVariable = b"Hello" #bytes is immutable
print(bytesVariable)
print(type(bytesVariable))

bytearrayVariable = bytearray(5) #bytearray is mutable
print(bytearrayVariable)
print(type(bytearrayVariable))

memoryviewVariable = memoryview(bytes(5)) #memoryview is mutable
print(memoryviewVariable)
print(type(memoryviewVariable))

