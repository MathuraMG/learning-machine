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

def feed_forward(l_weights, prev_l_output, l_bias) :
    l_activations = np.dot( l_weights, prev_l_output ) + l_bias
    l_output = activation_fn( l_activations )
    return l_output, l_activations

def back_propogate(l_activations,l_weights,l_delta,is_last_layer) :
    if is_last_layer:
        return activation_dfn(l_activations)*(l_weights-l_delta)
    else:
        return activation_dfn(l_activations)*np.dot(l_weights.T,l_delta)

def apply_delta(l_deltas,l_outputs,l_weights,l_bias):
    l_weights -= learning_rate * np.dot( l_deltas, l_outputs.T )
    l_bias -= learning_rate * l_deltas
    return l_weights, l_bias





activation_fn  = tanh_fn
activation_dfn = tanh_dfn

epoch = 0
reportFreq = 10000

learning_rate = 0.01

sample_size = 1
hidden_size = 15
# hidden1_size = 15
output_size = 1

layer_weights = []
layer_size = [sample_size, hidden_size, output_size]
def init_bias_weight(no_layers):
    for i in range(no_layers-1):
        print i
        layer_weights.append(np.random.rand( layer_size[i+1], layer_size[i] ))

error = np.zeros( ( sample_size, 1 ) )

# Initialize weights and biases:

init_bias_weight(3)
# layer0_weights = np.random.rand( hidden_size, sample_size )
layer0_bias = np.random.rand( hidden_size, 1 )

# layer1_weights = np.random.rand( output_size, hidden_size )
layer1_bias = np.random.rand( output_size, 1 )

# layer_weights = [layer0_weights, layer1_weights]

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
    layer1_outputs, layer1_activations = feed_forward(layer_weights[0],sample_vec,layer0_bias)

    # Feed forward (hidden to output):
    layer2_outputs, layer2_activations = feed_forward(layer_weights[1],layer1_outputs,layer1_bias)

    # Back propagate (output to hidden):
    # layer2_deltas = activation_dfn( layer2_activations ) * ( layer2_outputs - output_vec )
    layer2_deltas = back_propogate(layer2_activations,layer2_outputs,output_vec,True)

    # Back propagate (hidden to input):
    # layer1_deltas = activation_dfn( layer1_activations ) * np.dot( layer_weights[1].T, layer2_deltas )
    layer1_deltas = back_propogate(layer1_activations,layer_weights[1],layer2_deltas,False)

    # Apply deltas (layer 0):
    # layer_weights[0] -= learning_rate * np.dot( layer1_deltas, sample_vec.T )
    # layer0_bias -= learning_rate * layer1_deltas
    layer_weights[0], layer0_bias   = apply_delta(layer1_deltas,sample_vec, layer_weights[0],layer0_bias)

    # Apply deltas (layer 1):
    # layer_weights[1] -= learning_rate * np.dot( layer2_deltas, layer1_outputs.T )
    # layer1_bias -= learning_rate * layer2_deltas
    layer_weights[1], layer1_bias = apply_delta(layer2_deltas,layer1_outputs, layer_weights[1],layer1_bias)

    # Apply deltas (layer 1):
    # layer2_weights -= learning_rate * np.dot( layer3_deltas, layer2_outputs.T )
    # layer2_bias -= learning_rate * layer3_deltas

    # Compute error:
    error += np.absolute( output_vec - layer2_outputs )

    # Report error rate:
    if epoch % reportFreq == 0:
    	# print(layer_weights[1]);
    	# print(layer_weights[0]);
    	print( "Epoch: %d\nError: %f" % ( epoch, np.sum( error ) / float( sample_size ) / float( reportFreq ) ) )
    	error = np.zeros( ( sample_size, 1 ) )

    # Advance epoch iterator:
    epoch += 1
