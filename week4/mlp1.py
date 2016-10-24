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

class mlp():

    sample_size = 1
    hidden_size = 15
    # hidden1_size = 15
    output_size = 1
    error = []

    layer_weights = []
    layer_bias = []
    l_activations = []
    l_outputs = []
    l_deltas = []
    epoch = 1
    no_layers =1
    layer_size = []

    def init_deltas(self):
        for i in range(self.no_layers -1):
            self.l_deltas.append(1)

    def init_bias_weight(self,no_layers):
        # layer_size = [self.sample_size, self.hidden_size, self.output_size]
        for i in range(no_layers-1):
            print i
            self.layer_weights.append(np.random.rand( self.layer_size[i+1], self.layer_size[i] ))
            self.layer_bias.append(np.random.rand(self.layer_size[i+1],1))

    def init(self,user_epoch,no_layers,layer_size):
        self.epoch = user_epoch
        self.no_layers = no_layers
        self.layer_size = layer_size
        self.init_bias_weight(self.no_layers)
        self.init_deltas()
        self.error = np.zeros( ( self.sample_size, 1 ) )

    def feed_forward(self,l_weights, prev_l_output, l_bias) :
        l_activations = np.dot( l_weights, prev_l_output ) + l_bias
        l_output = activation_fn( l_activations )
        return l_output, l_activations

    def back_propogate(self,l_activations,l_weights,l_delta,is_last_layer) :
        if is_last_layer:
            return activation_dfn(l_activations)*(l_weights-l_delta)
        else:
            return activation_dfn(l_activations)*np.dot(l_weights.T,l_delta)

    def apply_delta(self,l_deltas,l_outputs,l_weights,l_bias):
        l_weights -= learning_rate * np.dot( l_deltas, l_outputs.T )
        l_bias -= learning_rate * l_deltas
        return l_weights, l_bias

    def single_loop(self, sample_vec, output_vec):
        #feed forwards
        self.l_activations = []
        self.l_outputs = []
        ip = sample_vec
        self.l_outputs.append(ip)
        for i in range(self.no_layers-1):
            l_op, l_act = self.feed_forward(self.layer_weights[i],self.l_outputs[i],self.layer_bias[i])
            self.l_outputs.append(l_op)
            self.l_activations.append(l_act)

        #back propogation
        for i in range(self.no_layers-1):
            j = self.no_layers - 1 - i
            if i==0:
                # print self.l_deltas
                self.l_deltas[j-1] = self.back_propogate(self.l_activations[j-1], self.l_outputs[j], output_vec, True)
            else:
                self.l_deltas[j-1] = self.back_propogate(self.l_activations[j-1],self.layer_weights[j],self.l_deltas[j],False)

        #apply deltas
        for i in range(self.no_layers-1):
            self.layer_weights[i], self.layer_bias[i]  = self.apply_delta(self.l_deltas[i],self.l_outputs[i], self.layer_weights[i],self.layer_bias[i])

        #error calc
        self.error +=  np.absolute( output_vec - self.l_outputs[self.no_layers-1] )

    def error_report(self,curr_epoch,reportFreq):
        # Report error rate:
        if epoch % reportFreq == 0:
        	print( "Epoch: %d\nError: %f" % ( curr_epoch, np.sum( self.error ) / float( self.sample_size ) / float( reportFreq ) ) )
        	self.error = np.zeros( ( self.sample_size, 1 ) )

activation_fn  = tanh_fn
activation_dfn = tanh_dfn

epoch = 0
reportFreq = 10000

learning_rate = 0.01

# Initialize mlp:
mlp1 = mlp()
error = np.zeros( ( mlp1.sample_size, 1 ) )
mlp1.init(1e6,4,[1,15,15,1])

while epoch <= mlp1.epoch :

    sample_vec = np.random.uniform( 0.0, np.pi * 2.0, ( mlp1.sample_size, 1 ) )
    # Compute output:
    output_vec = np.sin( sample_vec )

    mlp1.single_loop(sample_vec,output_vec)
    mlp1.error_report(epoch,reportFreq)
    # Advance epoch iterator:
    epoch += 1
