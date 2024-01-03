# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:45:33 2022

@author: kp503
"""
import numpy as np
import matplotlib.pyplot as plt

#Sigmoid
def sigmoid(trainData):
    return 1 / (1 + np.exp(-trainData))

#Derivative
def sigmoid_derivative(trainData):
    return trainData * (1 - trainData)

#The cost function to plot at the end
def costFunc(trainDataOutputPredict, trainDataOutputReal):
    return np.mean((trainDataOutputPredict - trainDataOutputReal) ** 2)


#Begins by setting up all the weights and biases, randomising them to begin with.
class NeuralNetwork:
    def __init__(self, inputLayer, hiddenLayer, outputLayer):
        self.inputLayer = inputLayer
        self.hiddenLayer = hiddenLayer
        self.outputLayer = outputLayer
        #setting up the layers and randomising weights
        self.W1 = np.random.randn(self.inputLayer, self.hiddenLayer)
        self.W2 = np.random.randn(self.hiddenLayer, self.outputLayer)
        
        #defining our neurons and being ready to run the training data through the code
    def forwardPropagation(self, trainData):
        self.z = np.dot(trainData, self.W1)
        self.z2 = sigmoid(self.z)
        self.z3 = np.dot(self.z2, self.W2)
        sigma = sigmoid(self.z3)
        return sigma
    #completeing backprop
    def backPropagation(self, trainData, trainDataOutput, sigma):
        self.sigmaError = trainDataOutput - sigma
        self.sigmaDelta = self.sigmaError * sigmoid_derivative(sigma)
        #finding our errors
        self.z2_error = self.sigmaDelta.dot(self.W2.T)
        self.z2_delta = self.z2_error * sigmoid_derivative(self.z2)
        #ammending the weights
        self.W1 += trainData.T.dot(self.z2_delta)
        self.W2 += self.z2.T.dot(self.sigmaDelta)
        
    def train(self, trainData, trainDataOutput, batch_size=5, epochs=10000):
        costHistory = []
        #sets up our mini batches in batches of 5
        for epoch in range(epochs):
            for i in range(0, len(trainDataOutput), batch_size):
                sigma = self.forwardPropagation(trainData[i:i+batch_size])
                self.backPropagation(trainData[i:i+batch_size], trainDataOutput[i:i+batch_size], sigma)
            #final prints and graphs to output at the end
            trainDataOutputPredict = self.predict(trainData)
            cost = costFunc(trainDataOutputPredict, trainDataOutput)
            costHistory.append(cost)
            
        return costHistory
                #running the training data
    def predict(self, trainData):
        return self.forwardPropagation(trainData)

# Define the input and output data
trainData = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
trainDataOutput = np.array([[0], [1], [1], [0]])
testData = np.array([[0, 1]])

# Create the neural network object
network = NeuralNetwork(inputLayer=2, hiddenLayer=4, outputLayer=1)

#running our training batches
network.train(trainData, trainDataOutput, batch_size=5, epochs=10000)
costHistory = network.train (trainData, trainDataOutput)
#printing our test data
print("the test data used is", testData)
print("the programs output of the test data is", network.predict(testData))

plt.figure()
plt.plot(costHistory)
plt.xlabel("EPOCHS")
plt.ylabel("Loss value")
plt.show()