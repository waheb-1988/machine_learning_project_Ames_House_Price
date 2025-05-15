import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer, KNNImputer, IterativeImputer

class MissingValueHandler:
    def __init__(self, df):
        self.df = df.copy()
    
    def drop_columns(self, threshold=0.5):
        """Drop columns with more than a certain percentage of missing values."""
        missing_fraction = self.df.isnull().mean()
        self.df = self.df.loc[:, missing_fraction < threshold]
        return self.df
    
    def drop_rows(self):
        """Drop rows containing any missing values."""
        return self.df.dropna()
    
    def fill_with_mean(self, column):
        """Fill missing values in a numerical column with the mean."""
        self.df[column] = self.df[column].fillna(self.df[column].mean())
        return self.df
    
    def fill_with_median(self, column):
        """Fill missing values in a numerical column with the median."""
        self.df[column] = self.df[column].fillna(self.df[column].median())
        return self.df
    
    def fill_with_mode(self, column):
        """Fill missing values in a categorical column with the mode."""
        self.df[column] = self.df[column].fillna(self.df[column].mode()[0])
        return self.df
    
    def fill_with_group_mean(self, column, group_by):
        """Fill missing values using group-wise mean."""
        self.df[column] = self.df[column].fillna(self.df.groupby(group_by)[column].transform('mean'))
        return self.df
    
    def forward_fill(self, column):
        """Forward fill missing values."""
        self.df[column] = self.df[column].fillna(method='ffill')
        return self.df
    
    def backward_fill(self, column):
        """Backward fill missing values."""
        self.df[column] = self.df[column].fillna(method='bfill')
        return self.df
    
    def interpolate(self, column, method='linear'):
        """Fill missing values using interpolation."""
        self.df[column] = self.df[column].interpolate(method=method)
        return self.df
    
    def knn_imputation(self, n_neighbors=5):
        """Fill missing values using K-Nearest Neighbors Imputer."""
        imputer = KNNImputer(n_neighbors=n_neighbors)
        self.df.iloc[:, :] = imputer.fit_transform(self.df)
        return self.df
    
    def iterative_imputation(self):
        """Fill missing values using Iterative Imputer (MICE Algorithm)."""
        imputer = IterativeImputer()
        self.df.iloc[:, :] = imputer.fit_transform(self.df)
        return self.df
