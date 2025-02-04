languages = ['Python', 'Ruby', 'GoLang', 'Rust', 'JavaScript', 'C++', 'TypeScript']

print("printing using index")
print()
for index in range(len(languages)):    
    print('Current language : ', languages[index])

print()

print("printing using value")
print()

for i in languages:
    print('Current language : ', i)   

print()

print("printing pattern")
print()


for i in range(4):
    for j in range(4):
        print("#" , end= " ")

    print()