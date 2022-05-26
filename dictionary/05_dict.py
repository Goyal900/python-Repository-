# Check if a value exists in a dictionary
sample_dict = eval(input("enter the input in dictionary form"))
k = int(input("enter the integer input "))
if k in sample_dict.values():
    print(f'{k} present in a dict')