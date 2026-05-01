import random
a=int(input("Enter no.of teams:"))
teams=[]
print("Enter all the teams name:")
for i in range(a):
  t=input("Enter team name:")
  teams.append(t)
m=int(input("Enter No of teams meet:"))
matches=[]
for i in range(0,a-1):
  for j in range(i+1,a):
    for k in range(m):
      matches.append([teams[i],teams[j]])
random.shuffle(matches)
pos=1
for i in matches:
  print("Matches {} : {} vs {}".format(pos,i[0],i[1]))
  pos+=1
  
  
""" 
  5-teams
      IND PAK AUS AFG NZ
IND VS PAK(0,1)
IND VS AUS(0,2)
IND VS AFG(0,3)
IND VS NZ(0,4)

PAK VS AUS(1,2)
PAK VS AFG(1,3)
PAK VS NZ(1,4)

AUS VS AFG(2,3)
AUS VS NZ(2,4)

AFG VS NZ(3,4)
"""
  
  
