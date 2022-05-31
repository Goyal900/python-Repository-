import random
a=[]
n=int(input("enter the size"))
for i in range(n):
  v=int(input("enter the value"))
  a.append(v)
print(random.choice(a))
