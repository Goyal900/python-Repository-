# program to get minimum and maximum values from the dictionary 
dict = eval(input("enter the input in dictionary format"))
print("your given dictionary is below")
print(dict)
value = dict.values()
max = max(value)
min = min(value)
print(f'{max} is maximum value and {min} is minimum value from your dictionary')