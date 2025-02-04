word = input("Enter the word for counting vowels : ")

vowels = ['a', 'i', 'e', 'o' , 'u']

count = 0
for i in range(len(word)):
    if word[i] in vowels:
        count = count+1


print(f'There are {count} vowels in {word}')