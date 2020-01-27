# numpy, scipy

import numpy

a = numpy.arange(12)

print(a, type(a), a.shape)

a.shape = 3, 4

print(a, a[2], a[2, 1], a[:, 1], a.transpose())



