def prime(x):
    c=0
    if x==0:
        print("no is zero")
    for i in (2,x+1):
        if x%i==0:
            c=c+1
      
        return c

n=int(input("enter the number"))
c=prime(n)
if c==0:
    print("your gien number is prime")
else:
    print("your given number is not prime")
