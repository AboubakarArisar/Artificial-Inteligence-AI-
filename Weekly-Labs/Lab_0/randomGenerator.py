import random
#for generating random variable we need to import random module


#generating random number between 1 and 10
randomNumber = random.randrange(1,10)
print(randomNumber) #printing the random number

#generating with seed value , seed should be greater than the range of the random number
randomNumber = random.sample(range(1, 20),10)

print(randomNumber) #printing the random numbers using seed

#10 wont be included in the random number generated
