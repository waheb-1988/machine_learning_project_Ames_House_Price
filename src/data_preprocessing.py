
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np 
import pathlib
import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


class OutlierReplaceWithMedian(BaseEstimator,TransformerMixin):
    
    def __init__(self, threshold=1.5):
         
         self.threshold = threshold
         
    def fit(self,X,y=None):
        return self
    def transform(self,x):
        X = X.copy()
        for col in X.select_dtypes(include=["float64", "int64"]).columns:
            Q1 = X[col].quantile(0.25)
            Q3 = X[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - self.threshold * IQR
            upper_bound = Q3 + self.threshold * IQR

            # Replace outliers with the median
            median = X[col].median()
            X[col] = np.where((X[col] < lower_bound) | (X[col] > upper_bound), median, X[col])
        return X
    @staticmethod     
    def read_file(file_name : str )  -> pd.DataFrame:
        """
        summary
        """
        try:
            dir_folder = pathlib.Path().cwd().parent
            print(dir_folder)
            file_path  = dir_folder / "data" 
            print(file_path)
            df = pd.read_csv(os.path.join(file_path/file_name))
            return df
        except FileNotFoundError:
            print(f"Error: The file at '{file_name}' was not found.")
            raise
        except Exception as e:
            print(f"An error occurred: {e}")
            
            
cs = OutlierReplaceWithMedian()            
df = cs.read_file('insurance.csv')      
    
print(df.head())


# Outliers replace
# Inpute missing vale
# Processing steps
# Onehot and Catencawdin
# Pipeline
# Model
# hyper
# Save
# test
# Flask
# Streamlit
# Requiremet file 
# Env file 
# Chatbot

