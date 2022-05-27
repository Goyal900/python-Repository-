#finding the max value and min value of flattened array
import numpy as np
q=np.array(([1,2,3,4,5],[6,7,8,9,10]))
print(q)
f=np.ndarray.flatten(q)
print("the flattened array is ",f)
ma=f.max()
mi=f.min()
print("the max and min value of flattened array is ",ma,mi)