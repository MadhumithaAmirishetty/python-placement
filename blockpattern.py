a=0

for i in range(3):
    c=0
    for j in range(4-a):
        for z in range(5):
            print("*",end=" ")
            c=c+1
        print()
    print(c)
    a=a+1
    print()
