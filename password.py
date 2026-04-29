a=input("enter your password:")
up=0
lw=0
di=0
sp=0
if(len(a)>7):
    for i in a:
        if(i.isupper()):
            up=up+1
        elif(i.islower()):
            lw=lw+1
        elif(i.isdigit()):
            di=di+1
        else:
            sp=sp+1
    if(up>0 and lw>0 and di>0 and sp>0):
        print("STRONG!!")
else:
    print("NOT STRONG PASSWORD")
