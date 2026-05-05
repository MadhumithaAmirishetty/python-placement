class circle:
    def __init__(self):
        x=int(input("Enter radius: "))
        self.r=x
    def display(self):
        print("area is",3.14*self.r**2)
a=int(input("enter num of circle:"))
l=[]
for i in range(a):
    c=circle()
    l.append(c)
    c.display()
    print("____________")
