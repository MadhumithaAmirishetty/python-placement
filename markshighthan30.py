name=["Sand","Hru","Saniyaww","Madhu"]
marks=[40,50,40,30]
pos=1
for i in range(4):
    if(marks[i]>30):
        print("{}.{} has scored{}.%".format(pos,name[i],marks[i]))
        pos=pos+1
