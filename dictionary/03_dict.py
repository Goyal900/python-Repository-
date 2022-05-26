# converting two lists into a dictionary
keys = eval(input("enter the input in list form"))
values = eval(input("enter the input again in list form"))
dictionary = dict(zip(keys, values))
print("your converted dictionary from the two lists is below \n")
print(dictionary)