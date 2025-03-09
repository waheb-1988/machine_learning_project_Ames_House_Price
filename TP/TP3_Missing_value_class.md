# **Exercise: Handling Missing Values in a Dataset**
# Objective
The goal of this exercise is to apply different missing value handling techniques using the MissingValueHandler class on a sample dataset.

# Instructions
## Load the Dataset

- Use Pandas to create a DataFrame with missing values.
- Instantiate the MissingValueHandler Class

- Create an object of the MissingValueHandler class and pass the DataFrame.
- Perform the Following Operations

- Drop columns with more than 40% missing values.
- Drop rows containing any missing values.
- Fill missing numerical values with the mean of the column.
- Fill missing numerical values with the median of the column.
- Fill missing categorical values with the mode.
- Use forward fill and backward fill to handle missing values.
- Apply KNN imputation with n_neighbors=3.
- Apply Iterative Imputation.
- Compare Results

- Print the DataFrame before and after each imputation method.