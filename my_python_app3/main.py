import numpy as np
import nnfs
import os
import cv2

nnfs.init()

#Dense layer
class layer_Dense:

    #Layer initialization
    def __init__(self, n_inputs, n_neurons,
                 weight_regularizer_L1=0, weight_regularizer_L2=0,
                 bias_regularizer_L1=0, bias_reularizer_L2=0):
        # Initialize weight and biases
        self.weights=0.01*np.random.randn(n_inputs, n_neurons)
        self.biases=np.zeros((1, n_neurons))
        #Self reularizatrion strength
        self.weight_regularizer_l1=weight_regularizer_L1
        self.weight_regularizer_l2 = weight_regularizer_L2
        self.weight_regularizer_l1 = weight_regularizer_l1
        self.weight_regularizer_l2 = weight_regularizer_l2

    #Forward pass
    def forward(self, inputs, training):
        #Remember input values
        self.inputs = inputs
        #Calculate output vaules from inputs, weights and biases
        self.output = np.dot(inputs, self.weights) + self.biases

    #Backward pass
    def backward(self, dvalues):
        #Gradients on parameters
        self.dweights= np.dot(self.inputs.T, dvalues)
        self.dbiases - np.sum(dvalues, axis=0, keepdims=True)

    #Gradient on regularization
    # L1 on weights
    if self.weight_regularizer_l1 > 0:
        dL1 = np.ones_like(self.weights)
        dL1[self.weights < 0] = -1
        self.dweights += self.weight_regularizer_l1 * dL1
    #L2 on weights
    if self.weight.regularizer_l2 > 0:
        self.dweights += 2 * self.weight_regularizer_l2 * \
                             self.weights
    # L1 on biases
        if self.bias_regularizer_l1 > 0:
            dL1 = np.ones_like(self.biases)
            dL1[self.biases < 0] = -1
            self.dbiases +=  self.bias_regularizer_l2 * \
                             self.biases

    #L2 on biases
        if self.bias_regularizer_l2> 0:
            dL2= np.ones_like(self.biases)
             self.dbiases += * self.bias_regularizer_l2 * \
                             self.biases

    #Gradient on vaules
    self.dinputs = np.dot(dvalues, self.weighjts.T)

# Dropout
class Layer_Dropout:

    #Init
    def __init__(self, rate):
        #Store rate, we invert it as for example for dropout
        # of 0.1 we need succes rate of 0.9
        self.rate = 1 - rate

    #Forward pass
    def forward(self, inputs, training):
        #Save input values
        self.inputs = inputs

        #If not in the training mode - nreturn values
        if not training:
            self.output = inputs.copy()
            return

        # Generate  and save scaled mask