# Init array with input data [[1,1],[0,1],[1,0],[0,0]]
# Init array with o/p data [1,0,0,0]
# Create a random array with weights - including the bias [w0,w1,wb]
# Run a loop
#    Check error b/w sigma(wi*input[i]) and expected o/p

import numpy as np

ip_value = np.array([[1,1],[-1,1],[1,-1],[-1,-1]])
op_value = [1,1,1,-1] #testing or gate
ip_bias = 1

learning_constant = 0.01
weight = 0.9*np.random.random(2)+0.01
weight_bias = 0.9*np.random.random(1)+0.01
print weight

for i in range(1000):
	for j in range(len(ip_value)):
		actual_output = sum(ip_value[j]*weight) + weight_bias*ip_bias
		expected_output = op_value[j]
		error = expected_output - actual_output
		delta_weight = error*ip_value[j]
		delta_weight_bias = error*ip_bias
		weight = weight + delta_weight*learning_constant
		weight_bias = weight_bias + delta_weight_bias*learning_constant

	print weight
	print weight_bias
