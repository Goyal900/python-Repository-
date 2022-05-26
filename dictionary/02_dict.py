'''Write a program to create three dictionaries
 and concatenate them to create fourth dictionary'''
d1 = eval(input("enter the first  input in dictionary form  "))
d2 = eval(input("enter the second   input dictionary form "))
d3 = eval(input("enter the third  input dictionary form  "))
d4 = {}
for i in (d1,d2,d3):
    d4.update(i)
print(d4)