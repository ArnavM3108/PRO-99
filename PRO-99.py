name = input("Enter your name ")

elements = len(name)

for i in range(elements):
    for y in range(elements):
        if i == y:
            print(name[i] , sep=" " , end=" ")
        else: 
            print("*" , sep=" " , end=" ")

    print()
