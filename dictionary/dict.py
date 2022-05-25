#input of dictionary from user
a={}
size=int(input("enter the size of dictionary"))
for i in range(0,size):
  key=input("enter key")
  value=input("enter value")
  a[key]=value
print(a)
