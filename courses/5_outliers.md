# How to Handle Outliers?

Outliers are data points that deviate significantly from the rest of the data. They can affect the accuracy of predictions and should be treated appropriately. This involves either removing them or transforming them using a suitable technique.

# Why Handle Outliers?

- For linear models: Outliers can significantly affect parameter estimation in linear regression models, so handling them before fitting the model is advisable.

- When outliers are due to errors: Data entry or measurement errors should be addressed to prevent distortion in analysis.

- When outliers affect distribution assumptions: Outliers can violate statistical test assumptions, affecting results, especially in parametric tests that assume normality.

# When Not to Remove Outliers?

- Genuine data: Some outliers represent valid variations in data, and removing them may introduce bias.

- Robust models: Models like decision trees, random forests, and gradient boosting are less sensitive to outliers.

- Scarce data: When data is limited, removing outliers can lead to information loss.

- Interest in outliers: Outliers may be crucial in fraud detection and anomaly detection tasks.

- Exploratory Data Analysis (EDA): Outliers should be analyzed before removal to gain insights.

# When Not to Remove Outliers?

## Univariate Outliers
1. **Visual Inspection:**  
    Box plots, scatter plots, and histograms can help visually identify outliers.
2. **Z-score Method:**
```python
from scipy import stats
import numpy as np
z_scores = stats.zscore(df)
abs_z_scores = np.abs(z_scores)
outliers = df[abs_z_scores > 3]
```
3. **Modified Z-Score Method:**
Uses median and median absolute deviation (MAD) for better robustness.
4. **Interquartile Range (IQR) Method:**
```python
def outlier_thresholds(dataframe, col_name, q1=0.25, q3=0.75):
    quartile1 = dataframe[col_name].quantile(q1)
    quartile3 = dataframe[col_name].quantile(q3)
    iqr = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * iqr
    low_limit = quartile1 - 1.5 * iqr
    return low_limit, up_limit
```
5. **Grubbs' Test:**
Statistical test for detecting outliers in univariate datasets.
6. **Tukey’s Fences:**
Similar to IQR but with different multipliers for skewed distributions.
## Multivariate  Outliers 
1. **Density-Based Methods (DBSCAN):** 
```python
from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan.fit(data)
outliers = data[dbscan.labels_ == -1]
```
2. **Local Outlier Factor (LOF):**
```python
from sklearn.neighbors import LocalOutlierFactor
clf = LocalOutlierFactor(n_neighbors=20)
df['scores'] = clf.negative_outlier_factor_
```
3. **Isolation Forest:**
```python
from sklearn.ensemble import IsolationForest
def random_cut_forest(data, n_estimators=100, contamination=0.1):
    model = IsolationForest(n_estimators=n_estimators, contamination=contamination)
    model.fit(data)
    return model.decision_function(data)
```

4. **IMahalanobis Distance:** Measures the distance of each point from the centroid in multivariate space.

5. **Robust Random Cut Forest:** Effective for high-dimensional datasets.

6. **Cluster-Based Methods:** Identify outliers as points that do not belong to any cluster.

## Techniques to Handle Outliers

1. **Removing Outliers:** Deleting outliers can lead to data loss and should be used cautiously.

2. **Winsorization:** Replaces extreme values with the nearest non-outliers.
```python
from scipy.stats.mstats import winsorize
import numpy as np
data = np.array([10, 20, 30, 40, 500])
winsorized_data = winsorize(data, limits=[0.05, 0.05])
```

4. **Data Transformation:** Logarithmic or square root transformations can reduce the impact of outliers.

5. **Robust Statistical Methods:** Useful for handling heavy-tailed distributions and datasets with outliers.

# Conclusion

Outliers should be carefully evaluated before removal or transformation to maintain data integrity and avoid bias. Proper handling of outliers ensures better model performance and accurate statistical inferences.

