# Init array with input data [[1,1],[0,1],[1,0],[0,0]]
# Init array with o/p data [1,0,0,0]
# Create a random array with weights - including the bias [w0,w1,wb]
# Run a loop
#    Check error b/w sigma(wi*input[i]) and expected o/p

import numpy as np

ip_value = [[1,1]],[-1,1],[1,-1],[-1,-1]]
op_value = [1,1,1,-1]
learning_constant = 0.05
weights = np.random.random(2)

for i in range(10):
	for j in range(len(ip_value)):
		op_actual = sum(np.array(ip_value[j])*weights)
		error = (op_value[j]-op_actual)*learning_constant
		weights = weights + error
		print error
		print weights
	print "********"
