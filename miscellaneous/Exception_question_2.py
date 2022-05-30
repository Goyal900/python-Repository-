try:
  a=int(input("enter the value"))
  b=int(input("enter the value"))
  c=a/b
  print("c=",c)
except ZeroDivisionError:
  print("denominator is 0")
except ValueError:
  print("unable to convert string to int")
except:
  print("some unknown error")
