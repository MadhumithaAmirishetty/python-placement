name=["SanD","hRu","SARa"]
age=[23,11,24]
res=list(zip(age,name))
res1=sorted(res)
pos=1
for i in res1:
    print("Rank {}: {} age is {} years old".format(pos,i[1],i[0]))
    pos=pos+1
