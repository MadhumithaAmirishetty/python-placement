a="mayuk"
b="mrudul"

a1=list(a)
b1=list(b)
for i in range(len(a1)):
    for j in range(len(b1)):
        if a1[i]==b1[j]:
            a1[i]='@'
            b1[j]='@'
            break
print(a1)
print(b1)
count=0
for k in a1:
    if k!='@':
        count=count+1
for k in b1:
    if k!='@':
        count=count+1
print(count)

index=0
r=list("FLAMES")
for i in range(5):
    index=(index+(count-1))%(len(r))
    r.pop(index)
print(r[0])
