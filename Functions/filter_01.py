def thrice(x):
    if x%3==0 and x%4==0:
        return thrice

n=eval(input("enter the correct format of list"))
s=list(filter(thrice,n))
print(s)