# 메모리 뷰


import array

numbers = array.array('h', [-2, -1, 0, 1, 2])

memv = memoryview(numbers)



print(memv.tolist(), len(memv))

print(memv.itemsize)

print(memv[0])

memv_oct = memv.cast('B')

print(memv_oct.tolist())
memv_oct[5]=4
print(memv_oct.tolist())
print(numbers)



