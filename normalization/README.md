# Data normalization:

Scaling just changes the range of your data. Normalization is a more radical transformation. The point of normalization is to change your observations so that they can be described as a normal distribution.
you'll normalize your data if you're going to be using a machine learning or statistics technique that assumes your data is normally distributed. The method we're using to normalize here is called the Box-Cox Transformation.

**`Note that:`**
* Box-Cox Transformation requires the data to be positive.
* If your data contains zero or negative values, you may need to perform some data preprocessing or choose a different transformation method.

**`After normalization: `**

* the value of mean equal value of median this indicates that it is normal distributed.
* the value of mean not equal 0 and value of std not equal 1 this indicates that it isn't standard distributed.
* the shape of our data has changed. after normalizing it looks more like the outline of a bell (hence "bell curve").
