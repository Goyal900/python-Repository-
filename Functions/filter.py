def iseven(x):
    if x%2==0:
        return iseven

l=eval(input("enter your correct format of list"))
l1=list(filter(iseven,l))
print(l1)