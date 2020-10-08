**Problem Statement**

This assignment calls for building a complete neural network using Numpy. It implements all the steps required to build a network - *feedforward, loss computation, backpropagation, weight updates* etc.

The assignment has provided with some starter code and the solution has been coded in cells marked '#Graded' .

The training is done using the MNIST dataset to classify handwritten digits between 0-9.
 
The assignment is divided into the following sections:

    Data preparation
    Feedforward
    Loss computation
    Backpropagation
    Parameter updates
    Model training and predictions


**Data Preparation**

No new code was written for this part.

Firstly, we load the data using the function load_data(). The function data_wrapper() is then applied to the data to get the train and test data in the desired shape. Please note that the code needs to take a batch of data points as the input. Hence, be careful while checking the dimensions.

There are 28x28 greyscale images in the MNIST dataset. Hence, each input image is a vector of length 784. The ground truth labels of a batch are stored in a matrix which is converted to a one-hot matrix. Also, the output of the model is a softmax output of length 10. 


Hence, we have the following:

train_set_x shape: (784, 50000)
train_set_y shape: (10, 50000)
test_set_x shape: (784, 10000)
test_set_y shape: (10, 10000)

**Feedforward**

There are functions assigned to different subparts of feedforward. 

    * The whole data is taken as one batch. No minibatch gradient descent is performed.
    * The cumulative input to the layer Zl is now a step in feedforward
    * The output of the last layer is denoted as HL instead of P where layer L is the final output layer. Hence, there are L−1 hidden layers.
    * For each layer l, the Zl is stored as 'activation_memory' and Hl−1, Wl, bl are stored as 'linear_memory' to use later in backpropagation

Summarization of the feedforward algorithm as above:

    H0=B
    for l in [1,2,.......,L−1]:
        Zl=Wl.Hl−1+bl
        Hl=σ(Zl)
    HL = softmax(WL.HL−1+bL)

Summarization of all the functions defined in feedforward:
| Function | Arguments | Returns | Explanation |
|----------|-----------|---------|-------------|
| sigmoid | Z | H, sigmoid_memory | Applies sigmoid activation on Z to calculate H. Returns H, sigmoid_memory = Z  (Step 2.2) |
|----------|-----------|---------|-------------|
| relu | Z | H, relu_memory | Applies relu activation on Z to calculate H. Returns H, relu_memory = Z  (Step 2.2) |
