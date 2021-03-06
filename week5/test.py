#!/usr/bin/python

# Learning Machines
# Taught by Patrick Hebron at NYU ITP
# Implementation based off of mlp.py

import numpy as np
import matplotlib.pyplot as plt
import random as random
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
		# title = 'Epoch: %d, Error: %f' % ( epoch, error )
		title = error
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

	sample_size = 4
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

	vis_ip = []
	vis_op = []
	vis_exp_op = []

	def init_deltas(self):
		for i in range(self.no_layers -1):
			self.l_deltas.append(1)

	def init_bias_weight(self,no_layers):
		# layer_size = [self.sample_size, self.hidden_size, self.output_size]
		for i in range(no_layers-1):
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
		print output_vec, self.l_outputs[self.no_layers-1]
		self.error +=  np.absolute( output_vec - self.l_outputs[self.no_layers-1] )


	def error_report(self,curr_epoch,reportFreq,input,output,vis):
		#  vis,input,output,predicted_output):
		# Report error rate:
		if epoch % reportFreq == 0:
			# print( "Epoch: %d\nError: %f" % ( curr_epoch, np.sum( self.error ) / float( self.sample_size ) / float( reportFreq ) ) )
			print self.error, epoch
			self.error = np.zeros( ( self.sample_size, 1 ) )
			# print(len(self.vis_ip))
			# vis.update(curr_epoch, self.error,self.vis_ip,self.vis_exp_op,self.vis_op)
			# self.vis_ip = []
			# self.vis_op = []
			# self.vis_exp_op = []

		# else:
		# 	print ''
			# self.vis_ip.append(input)
			# self.vis_op.append(self.l_outputs[self.no_layers-1])
			# self.vis_exp_op.append(output)

activation_fn  = sigmoid_fn
activation_dfn = sigmoid_dfn

epoch = 0
reportFreq = 1000

learning_rate = 0.05

# Initialize mlp:
mlp1 = mlp()
error = np.zeros( ( mlp1.sample_size, 1 ) )
mlp1.init(1*1e6,3,[4,5,1])
vis = MlpVisualizer(0,0.05,-1,2,reportFreq)

#get the data from dataset
j = 0
temp = []
for line in open('occupancy_data/datatest1.txt'):
	(ip0,ip1,ip2,ip3,ip4,op) = line.split(',')[2:8]
	# (ip0 ,ip1, ip2, op) = line.split(',')[0:4]
	temp.append( np.array([float(ip0)/100,float(ip1)/100,float(ip3)/2000,float(ip4),float(op) ]))
len_dataset = len(temp);


while epoch <= 0 : # mlp1.epoch :

	a = int(random.uniform(0,len_dataset-100))
	sample_vec = np.random.uniform( 0.0, np.pi * 2.0, ( mlp1.sample_size, 1 ) )
	# Compute output:
	output_vec = np.random.uniform( 0.0, np.pi * 2.0, ( mlp1.output_size, 1 ) )

	sample_vec[0][0] = np.array(temp[a][0:1])
	sample_vec[1][0] = np.array(temp[a][1:2])
	sample_vec[2][0] = np.array(temp[a][2:3])
	sample_vec[3][0] = np.array(temp[a][3:4])
	# sample_vec[4][0] = np.array(temp[a][4:5])
	output_vec[0][0] = np.array(temp[a][4:5])

	mlp1.single_loop(sample_vec,output_vec)
	mlp1.error_report(epoch,reportFreq,sample_vec,output_vec,vis)
	# ,vis,sample_vec,output_vec,output_vec)
	# Advance epoch iterator:
	epoch += 1

print "TRAINED"

mlp1.layer_weights = [np.array([[ 0.17315693,  3.97934288, -1.39429779,  0.05876728],
       [ 0.60272453,  0.40983925,  0.64044582,  0.40540237],
       [ 0.38631689, -0.22663658,  1.11830108,  0.31488553],
       [-0.26283805,  5.16384334, -2.4367963 ,  0.911978  ],
       [ 0.30596035, -7.71537321,  7.46137388,  0.09856373]]), np.array([[ -3.81665052,  -0.39449994,   0.47955104,  -5.23866311,
         10.19272988]])]

print mlp1.layer_weights
#get the data from dataset
test = input("Print 1 to test")
if test == 1:

	a = int(random.uniform(len_dataset-100,len_dataset))
	sample_vec = np.random.uniform( 0.0, np.pi * 2.0, ( mlp1.sample_size, 1 ) )
	# Compute output:
	output_vec = np.random.uniform( 0.0, np.pi * 2.0, ( mlp1.output_size, 1 ) )

	sample_vec[0][0] = np.array(temp[a][0:1])
	sample_vec[1][0] = np.array(temp[a][1:2])
	sample_vec[2][0] = np.array(temp[a][2:3])
	sample_vec[3][0] = np.array(temp[a][3:4])
	# sample_vec[4][0] = np.array(temp[a][4:5])
	output_vec[0][0] = np.array(temp[a][4:5])

	mlp1.single_loop(sample_vec,output_vec)
	mlp1.error_report(epoch,reportFreq,sample_vec,output_vec,vis)


# [array([[ -1.11658316,  -6.63828173,  14.12352507,   0.16191703],
#        [  0.35403078,   1.04657695,  -0.2831504 ,   0.63514848],
#        [  0.16944457,   0.06375683,  -0.74500543,   0.11892377],
#        [  0.07533053,  -2.1790229 ,   1.27191267,   0.82881094],
#        [  0.36988362,   2.42039056,  -0.51204487,   0.85458273],
#        [ -0.42499659,   5.18804538,  -0.56230807,   0.94880529],
#        [ -0.19164678,   2.6604004 ,  -1.1583207 ,   0.80116845],
#        [ -0.06503517,   4.10065808,  -1.2459598 ,   0.65871425],
#        [ -0.18687173,   8.12066375,  -0.56649147,   0.75706004],
#        [  0.89865017,   9.26432871,  -3.73168239,   0.15414304],
#        [  0.3776219 ,  -2.42203089,   0.69489637,   0.49594558],
#        [  0.24843764,   6.57299286,  -0.98986943,   0.32826934],
#        [  1.02364297,  -9.32246217,   4.06921567,   0.76534497],
#        [ -0.39961952,  10.69623552,  -1.7300804 ,   0.28630099],
#        [  0.98712682, -13.59830906,   5.18490786,   0.35034111]]), array([[ 8.42317402, -0.83575616, -0.19006316,  1.44944032, -1.57493328,
#         -2.77627935, -1.6839459 , -2.29014822, -4.15194331, -4.4217652 ,
#          1.52217533, -3.36693868,  4.88813745, -5.16370112,  6.65323273]])]
