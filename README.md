# ASSESSMENT PROJECT - ENSEMBLE MATRIX PVT LTD

## Requirements:
1. Make a server that serves a REST model to classify the fashion MNIST dataset. 

    [Reference tutorial](https://www.tensorflow.org/tfx/tutorials/serving/rest_simple)

    a. Use Google Colab to train and download the model. The model will be saved to your google colab working directory.

    b. Download the entire model directory on your local machine.

    c. Follow the instructions in the Reference tutorial, and serve the tensorflow model in your machine.

2. Build a django app with one endpoint, that accepts a POST request.
Given an uploaded image, it should:

    a. Convert the image into a numpy array of shape (28, 28). [Reference for numpy](https://numpy.org/doc/)
    
    b. Resize the image to dimensions: (1, 28, 28, 1) [Use this  for reference](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html).

    c. Make requests to the tensorflow server, as per the Reference tutorial.

    d. Save the prediction.

    e. Make a django dashboard that shows:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;i. The uploaded image<br>
        &nbsp;&nbsp;&nbsp;&nbsp;ii. The actual label<br>
        &nbsp;&nbsp;&nbsp;&nbsp;iii. The prediction

Feel free to use any database you want.

## Addendum

1. No need to install tensorflow on your laptop, everything will be handled by google colab

2. You might need to install opencv to your system to convert the django uploaded image to a numpy array. (Please feel free to google around, you might find other, simpler ideas not involving opencv)
