# Standardization (z-score normalization):
Rescaling features so that they are about standard normally distributed is a common alternative to the min-max scaling we talked about above. To do this, we use a process called standardization to change the data so that its mean is 0 and its standard deviation is 1.

**`Note that:`**
* we use Standardization when our data follow normal distributed.
* Standardization can help identfy outliers, data point with Z-score above 3 or 4 is consedered outlier. can be used to calculate P-value and test hyphesis.


**`After normalization: `**

* the value of mean equal value of median this indicates that it is normal distributed.
* the value of mean equal 0 and value of std equal 1 this indicates that it's standard distributed.
* the shape of our data has changed. after normalizing it looks more like the outline of a bell (hence "bell curve").
