num = int(input("Enter the number : "))

fact = 1;

for i in range(num):
    fact = fact * (i+1)


print(f"The factorial of {num} is {fact}")