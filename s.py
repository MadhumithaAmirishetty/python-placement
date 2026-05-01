a=[[" " for i in range(11)] for i in range(11)]

for i in range(11):
    for j in range(11):
        if i==0:
            a[i][j]="*"
for i in range(11):
    for j in range(11):
        if j==0 and i<6:
            a[i][j]="*"
for i in range(11):
    for j in range(11):
        if i==5:
            a[i][j]="*"
for i in range(11):
    for j in range(11):
        if j==10 and i>5:
            a[i][j]="*"
for i in range(11):
    for j in range(11):
        if i==10:
            a[i][j]="*"
            
for i in range(11):
    for j in range(11):
        print(a[i][j],end=" ")
    print()
