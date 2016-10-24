#!/usr/bin/python

# Learning Machines
# Taught by Patrick Hebron at NYU ITP

import numpy as np

def sigmoid_fn(x):
	return 1.0 / ( 1.0 + np.exp( -x ) )

def sigmoid_dfn(x):
	y = sigmoid_fn( x )
	return y * ( 1.0 - y )

def tanh_fn(x):
	return np.sinh( x ) / np.cosh( x )

def tanh_dfn(x):
	return 1.0 - np.power( tanh_fn( x ), 2.0 )

def hello(test):
	print test

activation_fn  = tanh_fn
activation_dfn = tanh_dfn

epoch = 0
reportFreq = 10000

learning_rate = 0.01

sample_size = 1
hidden_size = 15
# hidden1_size = 15
output_size = 1

error = np.zeros( ( sample_size, 1 ) )

# Initialize weights and biases:

layer0_weights = np.random.rand( hidden_size, sample_size )
layer0_bias = np.random.rand( hidden_size, 1 )

layer1_weights = np.random.rand( output_size, hidden_size )
layer1_bias = np.random.rand( output_size, 1 )

# layer2_weights = np.random.rand( output_size, hidden1_size )
# layer2_bias = np.random.rand( output_size, 1 )

# Perform each epoch:
while epoch <= 1e6 :
	# hello('my space');
	# Choose a random input:
	sample_vec = np.random.uniform( 0.0, np.pi * 2.0, ( sample_size, 1 ) )
	# Compute output:
	output_vec = np.sin( sample_vec )

	# Feed forward (input to hidden):
	layer1_activations = np.dot( layer0_weights, sample_vec ) + layer0_bias
	layer1_outputs = activation_fn( layer1_activations )

	# Feed forward (hidden to output):
	layer2_activations = np.dot( layer1_weights, layer1_outputs ) + layer1_bias
	layer2_outputs = activation_fn( layer2_activations )

	# Feed forward (hidden to output):
	# layer3_activations = np.dot( layer2_weights, layer2_outputs ) + layer2_bias
	# layer3_outputs = activation_fn( layer3_activations )

	# layer3_deltas = activation_dfn( layer3_activations ) * ( layer3_outputs - output_vec )

	# Back propagate (output to hidden):
	layer2_deltas = activation_dfn( layer2_activations ) * ( layer2_outputs - output_vec )

	# Back propagate (hidden to input):
	layer1_deltas = activation_dfn( layer1_activations ) * np.dot( layer1_weights.T, layer2_deltas )

	# Apply deltas (layer 0):
	layer0_weights -= learning_rate * np.dot( layer1_deltas, sample_vec.T )
	layer0_bias -= learning_rate * layer1_deltas

	# Apply deltas (layer 1):
	layer1_weights -= learning_rate * np.dot( layer2_deltas, layer1_outputs.T )
	layer1_bias -= learning_rate * layer2_deltas

	# Apply deltas (layer 1):
	# layer2_weights -= learning_rate * np.dot( layer3_deltas, layer2_outputs.T )
	# layer2_bias -= learning_rate * layer3_deltas

	# Compute error:
	error += np.absolute( output_vec - layer2_outputs )

	# Report error rate:
	if epoch % reportFreq == 0:
		# print(layer1_weights);
		# print(layer0_weights);
		print( "Epoch: %d\nError: %f" % ( epoch, np.sum( error ) / float( sample_size ) / float( reportFreq ) ) )
		error = np.zeros( ( sample_size, 1 ) )

	# Advance epoch iterator:
	epoch += 1
