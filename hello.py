import numpy as np
"""
x1 = np.linspace(1, 10)

x2 = np.linspace(1, 10, 10)

print(x1)
print(x2)

print("length of x1 is %d " % len(x1))
print("length of x2 id %d " % len(x2))
"""
from numpy.linalg import inv

a = np.array([[1., 2.], [3., 4.]]) 

ainv = inv(a)

print(np.allclose(np.dot(ainv, a), np.eye(2)))

# coding: utf-8
 
arr = np.arange(12).reshape((3, 4))
print ('array is:')
print (arr)
 
# 取第一维的索引 1 到索引 2 之间的元素，也就是第二行
# 取第二维的索引 1 到索引 3 之间的元素，也就是第二列和第三列
slice_one = arr[1:2, 1:3]
print ('first slice is:')
print (slice_one)
 
# 取第一维的全部
# 按步长为 2 取第二维的索引 0 到末尾 之间的元素，也就是第一列和第三列
slice_two = arr[:, ::2]
print ('second slice is:')
print (slice_two)

 
arr1 = np.arange(24).reshape((2, 3, 4))

print (arr1)
print()
print (arr1[0, 1,:])               # 等价于 arr[1, :, :]
print()
print (arr1[..., 1])            # 等价于 arr[:, :, 1]

