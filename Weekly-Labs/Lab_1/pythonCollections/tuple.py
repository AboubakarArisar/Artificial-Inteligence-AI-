tuple = (1,2,3,4,4,5)

print(tuple)
tuple2 = (6,75,8)
tuple = tuple.__add__(tuple2)
print(tuple)

print(tuple.count(4))
print(tuple.index(4))