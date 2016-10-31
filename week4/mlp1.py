#!/usr/bin/python

# Learning Machines
# Taught by Patrick Hebron at NYU ITP
# Implementation based off of mlp.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def sigmoid_fn(x):
	return 1.0 / ( 1.0 + np.exp( -x ) )

def sigmoid_dfn(x):
	y = sigmoid_fn( x )
	return y * ( 1.0 - y )

def tanh_fn(x):
	return np.sinh( x ) / np.cosh( x )

def tanh_dfn(x):
	return 1.0 - np.power( tanh_fn( x ), 2.0 )


# MLP Visualization Class:

class MlpVisualizer:
	def __init__(self,data_xmin,data_xmax,data_ymin,data_ymax,report_freq,buffer_size = 100):
		self.report_freq  = report_freq
		self.error_buffer = buffer_size
		# Setup plotter data:
		self.error_xdata = []
		self.error_ydata = []
		# Setup plotter:
		plt.ion()
		self.fig = plt.figure( 1 )
		self.fig.subplots_adjust( hspace = 0.3 )
		# Add subplots:
		self.datav_plot = self.fig.add_subplot( 1, 1, 1 )
		# self.error_plot = self.fig.add_subplot( 2, 1, 2 )
		# Setup predictions subplot:
		self.datav_plot.set_title( 'Predictions' )
		self.datav_targ_line = Line2D( [], [], color='green', marker='+', linestyle='None' )
		self.datav_pred_line = Line2D( [], [], color='red', marker='x', linestyle='None' )
		self.datav_plot.add_line( self.datav_targ_line )
		self.datav_plot.add_line( self.datav_pred_line )
		self.datav_plot.set_xlim( data_xmin, data_xmax )
		self.datav_plot.set_ylim( data_ymin, data_ymax )
		# Setup error rate subplot:
		# self.error_plot.set_xlabel( 'Epoch' )
		# self.error_plot.set_ylabel( 'Error' )
		# 	self.error_line = Line2D( [], [], color='black' )
		# self.error_plot.add_line( self.error_line )
		# self.error_plot.set_ylim( 0.0, 1.0 )
		# Show plot:
		plt.show()

	def saveImage(self,filepath):
		plt.savefig( filepath )

	def update(self,epoch,error,input,target,output):
		# Update error plotter data:
		if len( self.error_xdata ) == self.error_buffer:
			self.error_xdata.pop( 0 )
			self.error_ydata.pop( 0 )
		self.error_xdata.append( epoch )
		self.error_ydata.append( error )
		#
		title = 'Epoch: %d, Error: %f' % ( epoch, error )
		# self.error_plot.set_title( title )
		# Compute error plotter x-range:
		# mlen = self.report_freq * self.error_buffer
		# xmin = np.amin( self.error_xdata )
		# xmax = max( xmin + mlen, np.amax( self.error_xdata ) )
		# Update error plotter:
		# self.error_line.set_data( self.error_xdata, self.error_ydata )
		# self.error_plot.set_xlim( xmin, xmax )
		# Update predictions plotter:
		self.datav_targ_line.set_data( input, target )
		self.datav_pred_line.set_data( input, output )
		# Draw plot:
		plt.draw()
		plt.pause( 0.01 )


class mlp():

	sample_size = 1
	hidden_size = 2
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

	vis_ip = []
	vis_op = []
	vis_exp_op = []

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

	def error_report(self,curr_epoch,reportFreq,input,output,vis):
		#  vis,input,output,predicted_output):
		# Report error rate:
		if epoch % reportFreq == 0:
			print( "Epoch: %d\nError: %f" % ( curr_epoch, np.sum( self.error ) / float( self.sample_size ) / float( reportFreq ) ) )
			self.error = np.zeros( ( self.sample_size, 1 ) )
			print(len(self.vis_ip))
			vis.update(curr_epoch, self.error,self.vis_ip,self.vis_exp_op,self.vis_op)
			self.vis_ip = []
			self.vis_op = []
			self.vis_exp_op = []

		else:
			self.vis_ip.append(input)
			self.vis_op.append(self.l_outputs[self.no_layers-1])
			self.vis_exp_op.append(output)

activation_fn  = tanh_fn
activation_dfn = tanh_dfn

epoch = 0
reportFreq = 1000

learning_rate = 0.05

# Initialize mlp:
mlp1 = mlp()
error = np.zeros( ( mlp1.sample_size, 1 ) )
mlp1.init(1e6,3,[1,2,1])  # best size for hidden layer should be between average of sample and op vec size -> 2* sample vec size
vis = MlpVisualizer(0,7,-2,2,reportFreq)

while epoch <= mlp1.epoch :

	sample_vec = np.random.uniform( 0.0, np.pi * 2.0, ( mlp1.sample_size, 1 ) )
	# Compute output:
	output_vec = (np.sin( sample_vec )*np.sin( sample_vec ) + np.cos( sample_vec ))/2

	mlp1.single_loop(sample_vec,output_vec)
	mlp1.error_report(epoch,reportFreq,sample_vec,output_vec,vis)
	# ,vis,sample_vec,output_vec,output_vec)
	# Advance epoch iterator:
	epoch += 1
