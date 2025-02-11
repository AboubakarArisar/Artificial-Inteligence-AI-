from array import *

temps = array ('i', [3,2,4,5,67,7])

for i in temps:
    print(i)



temps.append(45)
print(temps)
temps.insert(0,1)
print(temps)
temps.remove(67)
print(temps)
print(temps.index(5))
