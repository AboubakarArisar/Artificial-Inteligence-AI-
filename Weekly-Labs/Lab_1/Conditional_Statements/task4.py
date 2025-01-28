age = int(input("Enter the age : "))

if age < 0:
    print("age can't be lesss than zero")
else:
    if age < 13:
        print("You are a child")
    elif age >= 13 and age < 20:
        print("You are a teenager")
    else:
        print("You are an adult")