import numpy as np

data = np.array([
		[0,1,2],
		[3,4,5]
	])

print(data)
print(data.ndim)
print(data.shape)
print(np.average(data,axis=0))