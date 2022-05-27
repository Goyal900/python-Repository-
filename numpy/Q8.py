#finding the difference of max value and min value of array along second axis
import numpy as np
a=np.array(([1,2,3,4,5],[6,7,8,9,10]))
print(a)
m=np.amax(a,1)
mi=np.amin(a,1)
difference=m-mi
print("the difference between the max value and min value of the array along the second axis is ",difference)