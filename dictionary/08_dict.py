# write a program to print the sum of key vakue pairs in dictionary 
dict = eval(input("enter the input in dictionary form"))
print("your given dictionary is below ",dict)

sumlist=[]
for key in dict:
    sumlist.append(key + dict[key])
print("the sum of your dictionary's key value pairs is below")
print(sumlist)
