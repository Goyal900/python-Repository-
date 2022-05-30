while True:
  try:
    num=int(input("enter the value"))
    break
  except ValueError:
    print("incorrect input")
print("you entered",num)
