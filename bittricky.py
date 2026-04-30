name=["SanD","hRu","SARa"]
marks=[[40,85,40],[40,60,50],[20,30,50]]
pos=1
for i in range(3):
    avg=(sum(marks[i])//len(marks[i]))
    if(avg>80):
        print("{}.Ms/Mr {} has scored {}.% - S Grade".format(pos,name[i].title(),avg))
    elif(avg>40 and avg<60):
        print("{}.Ms/Mr {} has scored {}.% - B Grade".format(pos,name[i].title(),avg))
    elif(avg>60 and avg>80):
        print("{}.Ms/Mr {} has scored {}.% - A Grade".format(pos,name[i].title(),avg))
    else:
          print("{}.Ms/Mr{} has scored {}.% - Failed".format(pos,name[i].title(),avg))
    pos=pos+1
