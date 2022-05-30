def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
a=int(input("enter the value"))
b=int(input("enter the value"))
AbyB(a,b)
