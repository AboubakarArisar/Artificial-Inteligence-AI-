

def getPrime(number):
    factors = 0
    for i in range(number):
        if  (number) % (i+1) == 0:
            factors = factors + 1  

    if factors == 2:
        return True
    else:
        return False        
    
for i in range(50):
    if getPrime(i):
        print(i)
