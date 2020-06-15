<!-- Tensorflow basics -->

### What is tensoflow?

_TensorFlow is a free and open-source software library for dataflow and differentiable programming across a range of tasks. It is a symbolic math library, and is also used for machine learning applications such as neural networks._

We're going to use **keras**. Let's see what is this?

- **Keras** is a neural network library while **Tensorflow** is the open source library for a number of various tasks in machine learning.
- **Tensorflow** provides both high-level and low-level APIs while **Keras** provides only high-level APIs

This definitions are taken from google and official documentation of tensorflow. We'll follow the [official documentation](https://www.tensorflow.org/guide/keras "Learn keras") which is the best resource to learn tensorflow.

Let's not think much about this, we'll learn by practising things.

---

We're gonna use [Google Colab](https://colab.research.google.com/ "similar to Jupyter Notebook") for this tutorial. It is a free cloud service that requires no setup to use.

Let's install it first.

> `!pip install tensorflow`

1. Now import the followings:

```python
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
```

2. We need some data to work with. There is a dataset called [Fashion-MNIST](https://research.zalando.com/welcome/mission/research-projects/fashion-mnist/) which is inside keras and we'll use it in this tutorial. There are bunch of datasets to work with. Now let's load this data.

> `data = keras.datasets.fashion_mnist`

3. We need to split out data into traing data and test data.
   - First we'll train the data
   - Then we'll use test data to evaluate how accurate is the training.

> `(train_images, train_labels), (test_images, test_labels) = data.load_data()`

- _The images are 28x28 NumPy arrays, with pixel values ranging from 0 to 255._
- _The labels are an array of integers, ranging from 0 to 9._

![Labels](https://miro.medium.com/max/1200/1*ogbAotjStIKLG4TyLzzDtQ.png)

4. The result will be shown a value ranging between 0 to 9. As we don't know which label means what item, we can write the following code to store the label descriptions. I'm copying the code from [documnetation](https://www.tensorflow.org/tutorials/keras/classification).

   - We can do bunch of things with this data

   ```python
   print(len(train_images), len(test_images))
   print(train_images.shape, test_images.shape)
   ```

   The output will be like this:

   ```
    60000 10000
    (60000, 28, 28) (10000, 28, 28)
   ```

   - We can visualize the data using pyplot by writing this code

   ```
   plt.imshow(train_images[7], cmap=plt.cm.binary)
   plt.show()
   ```

   _Here, 7 is an arbitrary number_

![](images/fashion-1.JPG)
![](images/fashion-1cmap.JPG)

_without using cmap and using cmap_

5. Now we already know that pixel values ranging from 0 to 255, we can shrink our data dividing every value by 255. For numpy array it's just a one line of code

```
train_images = train_images/255.0
test_images = test_images/255.0
```

---

---

**Now the main task will begin**

_we'll train our model, test the accuracy_

But let's learn some theory first. Neural Network has 3 layers:

![input, hidden, output](https://i.pinimg.com/originals/f8/0e/41/f80e4134dd5af815b29abe79415d5dba.png)

- Before feeding values in the input layer, we need to flatten our data into 1D.
- As total label is 10 in the Fashion MNIST dataset, our output layer will be also 10.
- hidden layer value will be arbitrary

6. Let's see our code:

```python
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
```

- **Sequential:** -> indicating that three layers is added sequentially.
  - **Flatten:** transforms the format of the images from a two-dimensional array (of 28 by 28 pixels) to a one-dimensional array (of 28 \* 28 = 784 pixels).
  - **Dense:** densely connected, or fully connected, neural layers. The first Dense layer has 128 nodes (or neurons).
  - **relu:** activation is “relu” which means negative values will be thrown away.

7. We need another setup before training our model - _compiling the model_

```python
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```
