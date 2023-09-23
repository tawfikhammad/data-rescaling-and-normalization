# Data Rescaling

In machine learning, rescaling is a frequent pre-processing step. One of the simplest methods of rescaling is known as `min-max scaling`. A feature’s minimum and maximum values are used to rescale data to fit inside a predetermined range when using min-max scaling.

```
scaled_value = (value - min_value) / (max_value - min_value)
```

**min-max scaling** gives accurate results when:
* the standard deviation is low
* distribution doesn't follow the Gaussian model.

**`Note that`** : the shape of the data doesn't change, but the range of data.

This strategy is quite sensitive to data that contains outliers.




