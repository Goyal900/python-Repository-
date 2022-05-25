#sorting the dictionary by key
a={}
size=int(input("enter the size of dictionary"))
for i in range(0,size):
  key=input("enter key")
  value=input("enter value")
  a[key]=value
print(a)
b=sorted(a.keys())
print(b)
