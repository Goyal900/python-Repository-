#finding the frequency of 'p' in given array
import numpy as np
c=[]
a=np.array(['p','q','r','t','p','y','p'])
for i in a:
  if i =='p':
    c.append(i)
frequency=len(c)
print("the number of occurences of 'p' in the given array is ",frequency)