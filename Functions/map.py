def thrice(f):
    return f*3
lis=eval(input("plz enter the correct ordered list"))
s=list(map(thrice,lis))
print(s)
print(s.sort())