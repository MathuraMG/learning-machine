# Init array with input data [[1,1],[0,1],[1,0],[0,0]]
# Init array with o/p data [1,0,0,0]
# Create a random array with weights - including the bias [w0,w1,wb]
# Run a loop
#    Check error b/w sigma(wi*input[i]) and expected o/p

import numpy as np

#AND gate
ip_value = np.array([[1,1],[-1,-1],[1,-1],[-1,1]])
op_value = np.array([1,-1,-1,-1])

learning_constant = 0.1;

weight = np.random.random(2);
print weight
print '********'

for j in range(1000):
    for i in range(len(ip_value)):
        actual_output = sum(ip_value[i]*weight)
        expected_output = op_value[i]
        error = expected_output - actual_output
        delta_weight = error*ip_value[i]
        weight = weight + delta_weight*learning_constant

        print error
        print weight
