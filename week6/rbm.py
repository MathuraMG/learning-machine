#!/usr/bin/python

# Learning Machines
# Taught by Patrick Hebron at NYU ITP

import numpy as np

# Sigmoid function
def sigmoid(x):
    return 1.0 / ( 1.0 + np.exp( -x ) )

# Bernoulli Restricted Boltzmann Machine class
class RBM:
    def __init__(self, sizeV, sizeH):
        # Initialize random number generator:
        self.rng = np.random.RandomState()
        # Initialize weights:
        self.weights = np.array( self.rng.uniform( -1.0 / sizeV, 1.0 / sizeV, ( sizeV, sizeH ) ) )
        # Initialize biases:
        self.biasH   = np.zeros( sizeH )
        self.biasV   = np.zeros( sizeV )

    def train(self, data, training_epochs, learning_rate, cd_steps):
        # Perform each training epoch:
        for epoch in xrange( training_epochs ):
            # Get hidden activations and samples:
            aH_0, sH_0 = self.getHiddenSample( data )
            # Perform each contrastive divergence step:
            for i in xrange( cd_steps ):
                aV_inf, sV_inf, aH_inf, sH_inf = self.getGibbsHvh( ( sH_0 if i == 0 else sH_inf ) )
            # Update weights:
            self.weights += learning_rate * ( np.dot( data.T, aH_0 ) - np.dot( sV_inf.T, aH_inf ) )
            # Update biases:
            self.biasV   += learning_rate * np.mean( data - sV_inf, axis = 0 )
            self.biasH   += learning_rate * np.mean( aH_0 - aH_inf, axis = 0 )

    def getHiddenActivations(self, inputV):
        return sigmoid( np.dot( inputV, self.weights ) + self.biasH )

    def getVisibleActivations(self, inputH):
        return sigmoid( np.dot( inputH, self.weights.T ) + self.biasV )

    def getHiddenSample(self, inputV):
        aH = self.getHiddenActivations( inputV )
        sH = self.rng.binomial( 1, aH, aH.shape )
        return [ aH, sH ]

    def getVisibleSample(self, inputH):
        aV = self.getVisibleActivations( inputH )
        sV = self.rng.binomial( 1, aV, aV.shape )
        return [ aV, sV ]

    def getGibbsHvh(self, inputH):
        aV, sV = self.getVisibleSample( inputH )
        aH, sH = self.getHiddenSample( sV )
        return [ aV, sV, aH, sH ]

    def getGibbsVhv(self, inputV):
        aH, sH = self.getHiddenSample( inputV )
        aV, sV = self.getVisibleSample( sH )
        return [ aH, sH, aV, sV ]

    def getReconstruction(self, inputV):
        aH = self.getHiddenActivations( inputV )
        aV = self.getVisibleActivations( aH )
        return aV


# RBM Usage example:

# Initialize training data:
data_train = np.array([
    [1,1,1,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0],
    [1,0,1,0,0,0,0,0,0],
    [0,0,0,1,1,1,0,0,0],
    [0,0,0,1,1,1,0,0,0],
    [0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,1,1,1],
    [0,0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,1,1,0]
])

# Initialize testing data:
data_test = np.array([
    [1,1,1,0,0,0,0,0,0],
    [0,1,1,0,0,0,0,0,0],
    [0,0,0,1,1,1,0,0,0],
    [0,0,0,1,0,1,0,0,0],
    [0,0,0,0,0,0,1,1,1],
    [0,0,0,0,0,0,0,1,1]
])

# Set network parameters:
visible_size    = 9
hidden_size     = 4
training_epochs = 10000
learning_rate   = 0.01
cd_steps        = 1

# Initialize RBM:
rbm = RBM( visible_size, hidden_size )

# Train RBM:
rbm.train( data_train, training_epochs, learning_rate, cd_steps )

# Perform Gibbs sampling:
aH, sH, aV, sV = rbm.getGibbsVhv( data_test )

# Set print formatting:
np.set_printoptions( precision = 3, suppress = True )

# Print results:
print "Training Data:"
print data_train
print "Test Data:"
print data_test
print "Test Output Activations:"
print aV
print "Test Output Samples:"
print sV
