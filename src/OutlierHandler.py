import numpy as np
import pandas as pd
from scipy import stats
from sklearn.ensemble import IsolationForest

class OutlierHandler:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def detect_zscore(self, column, threshold=3):
        """Detects outliers using the Z-score method."""
        z_scores = np.abs(stats.zscore(self.dataframe[column]))
        return self.dataframe[z_scores > threshold]
    
    def detect_iqr(self, column):
        """Detects outliers using the IQR method."""
        q1 = self.dataframe[column].quantile(0.25)
        q3 = self.dataframe[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        return self.dataframe[(self.dataframe[column] < lower_bound) | (self.dataframe[column] > upper_bound)]
    
    def detect_isolation_forest(self, column, contamination=0.1):
        """Detects outliers using Isolation Forest."""
        model = IsolationForest(contamination=contamination, random_state=42)
        self.dataframe['outlier_score'] = model.fit_predict(self.dataframe[[column]])
        return self.dataframe[self.dataframe['outlier_score'] == -1]
    
    def remove_outliers(self, column, method='iqr'):
        """Removes outliers based on the selected method."""
        if method == 'zscore':
            outliers = self.detect_zscore(column)
        elif method == 'iqr':
            outliers = self.detect_iqr(column)
        elif method == 'isolation_forest':
            outliers = self.detect_isolation_forest(column)
        else:
            raise ValueError("Method not recognized")
        
        return self.dataframe.drop(outliers.index)
    
# Example usage:
if __name__ == "__main__":
    # Create sample data
    data = {'values': [10, 12, 13, 15, 14, 100, 102, 16, 18, 17, 200, 12]}
    df = pd.DataFrame(data)
    
    handler = OutlierHandler(df)
    print("Outliers using Z-score:\n", handler.detect_zscore('values'))
    print("Outliers using IQR:\n", handler.detect_iqr('values'))
    print("Outliers using Isolation Forest:\n", handler.detect_isolation_forest('values'))
