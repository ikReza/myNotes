We used 28\*28 = 784 pixel values to store our data. But we can see that there are lots of free spaces that don't contain any image information.

We can further improve our model by **pooling** and **convolutions**.

1. [Convolutions and pooling](https://youtu.be/PCgLmzkRM38)
2. This is a [good tutorial](https://youtu.be/7g8jpK4llkc) to undestand convolution
3. These are tutorials - ( [tutorial 1](https://youtu.be/8oOgPUO-TBY), [tutorial 2](https://youtu.be/PjtqcNr4T-Q) ) to undestand pooling

_pooling_ is an important way to reduce the amount of information our model has to process

#### What is the difference between convolutions and pooling?

- The major difference is a convolution filter is extracting features from the matrix of data, whereas the pooling layer is only downsampling the matrix of data.

- This means that if you include a large stride in the convolution filter, you are changing the types of features you extract in the algorithm, whereas if you change it in the pooling layer, you are simply changing how much the data is downsampled.

- [useful links](https://www.quora.com/Whats-the-difference-between-convolution-filter-with-large-stride-and-max-pooling-layer-as-both-down-sample-the-input-layer-when-to-use-each)

---

### Let's start coding.

For our convenience let's see the previous code again:

```python
import tensorflow as tf
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
training_images=training_images / 255.0
test_images=test_images / 255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(training_images, training_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels)
```

print out to see the results.

```python
print("Test loss: ", test_loss)
print("Test accuracy: ", test_acc * 100,"%")
```

output > `Test loss: 0.3359573781490326 Test accuracy: 87.79000043869019 %`

### Now we'll use convolutions to improve the accuracy

- **convolutions** narrow down the content of the image to focus on specific, distinct, details.

#### Here's the code:

```python
import tensorflow as tf
print(tf.__version__)
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
training_images=training_images.reshape(60000, 28, 28, 1)
training_images=training_images / 255.0
test_images = test_images.reshape(10000, 28, 28, 1)
test_images=test_images/255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(28, 28, 1)),
  tf.keras.layers.MaxPooling2D(2, 2),
  tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
model.fit(training_images, training_labels, epochs=5)
test_loss, test_acc = model.evaluate(test_images, test_labels)
```

Can you find out the difference between this code and the previous code?

- we've added extra 4 layers - convolution-1, pooling-1, convolution-2, pooling-2.
- There's another chnage. If you see the 5th and 7th line, we used reshape function.
- using _model.summary()_ we can see what's happening in every step.

_Step 1 is to gather the data. You'll notice that there's a bit of a change here in that the training data needed to be reshaped. That's because the first convolution expects a single tensor containing everything, so instead of 60,000 28x28x1 items in a list, we have a single 4D list that is 60,000x28x28x1, and the same for the test images. If you don't do this, you'll get an error when training as the Convolutions do not recognize the shape._

---

#### Quiz Quiz

1. What is a convolution

   - [ ] A technique to filter out unwanted images
   - [x] A technique to isolate features im images

2. What is a Pooling?

   - [x] A technique to reduce the information in an image while maintaining features
   - [ ] A technique to isolate features im images

3. Applying Convolutions on top of our Deep neural network will make training:
   - [ ] Faster
   - [x] It depends on many factors. It might make your training faster or slower, a poorly designed Convolutional layer may even be less efficient than a plain DNN!

---
