# Machine Learning Project: Ames Housing Data Set 


## Overview  
This project involves analyzing and building machine learning models using the Ames Housing Data Set. The primary objective is to explore the dataset, uncover valuable insights, and build predictive models to estimate house sale prices based on various features such as property size, location, condition, and amenities.  

## Project Objectives  
-Perform exploratory data analysis (EDA) to understand the dataset's features and distributions.
-Build predictive models to estimate house sale prices using machine learning algorithms.
-Evaluate and compare model performance using metrics such as Mean Absolute Error (MAE) and R-squared (R²).
-Derive actionable insights to help real estate professionals make data-driven decisions. 

## Dataset Description  
The dataset used in this project contains detailed information about residential properties in Ames, Iowa, including:

- **SalePrice:** The property's sale price in dollars (target variable).
- **MSSubClass:** The building class.
- **MSZoning:** The general zoning classification.
- **LotFrontage:** Linear feet of street connected to property.
- **LotArea:** Lot size in square feet.
- **Street:** Type of road access.
- **Alley:** Type of alley access.
- **LotShape:** General shape of property.
- **LandContour:** Flatness of the property.
- **Utilities:** Type of utilities available.
- **LotConfig:** Lot configuration.
- **LandSlope:** Slope of property.
- **Neighborhood:** Physical locations within Ames city limits.
- **Condition1:** Proximity to main road or railroad.
- **Condition2:** Proximity to main road or railroad (if a second is present).
- **BldgType:** Type of dwelling.
- **HouseStyle:** Style of dwelling.
- **OverallQual:** Overall material and finish quality.
- **OverallCond:** Overall condition rating.
- **YearBuilt:** Original construction date.
- **YearRemodAdd:** Remodel date.
- **RoofStyle:** Type of roof.
- **RoofMatl:** Roof material.
- **Exterior1st:** Exterior covering on house.
- **Exterior2nd:** Exterior covering on house (if more than one material).
- **MasVnrType:** Masonry veneer type.
- **MasVnrArea:** Masonry veneer area in square feet.
- **ExterQual:** Exterior material quality.
- **ExterCond:** Present condition of the material on the exterior.
- **Foundation:** Type of foundation.
- **BsmtQual:** Height of the basement.
- **BsmtCond:** General condition of the basement.
- **BsmtExposure:** Walkout or garden level basement walls.
- **BsmtFinType1:** Quality of basement finished area.
- **BsmtFinSF1:** Type 1 finished square feet.
- **BsmtFinType2:** Quality of second finished area (if present).
- **BsmtFinSF2:** Type 2 finished square feet.
- **BsmtUnfSF:** Unfinished square feet of basement area.
- **TotalBsmtSF:** Total square feet of basement area.
- **Heating:** Type of heating.
- **HeatingQC:** Heating quality and condition.
- **CentralAir:** Central air conditioning.
- **Electrical:** Electrical system.
- **1stFlrSF:** First floor square feet.
- **2ndFlrSF:** Second floor square feet.
- **LowQualFinSF:** Low-quality finished square feet (all floors).
- **GrLivArea:** Above grade (ground) living area square feet.
- **BsmtFullBath:** Basement full bathrooms.
- **BsmtHalfBath:** Basement half bathrooms.
- **FullBath:** Full bathrooms above grade.
- **HalfBath:** Half baths above grade.
- **Bedroom:** Number of bedrooms above basement level.
- **Kitchen:** Number of kitchens.
- **KitchenQual:** Kitchen quality.
- **TotRmsAbvGrd:** Total rooms above grade (excluding bathrooms).
- **Functional:** Home functionality rating.
- **Fireplaces:** Number of fireplaces.
- **FireplaceQu:** Fireplace quality.
- **GarageType:** Garage location.
- **GarageYrBlt:** Year garage was built.
- **GarageFinish:** Interior finish of the garage.
- **GarageCars:** Size of garage in car capacity.
- **GarageArea:** Size of garage in square feet.
- **GarageQual:** Garage quality.
- **GarageCond:** Garage condition.
- **PavedDrive:** Paved driveway.
- **WoodDeckSF:** Wood deck area in square feet.
- **OpenPorchSF:** Open porch area in square feet.
- **EnclosedPorch:** Enclosed porch area in square feet.
- **3SsnPorch:** Three season porch area in square feet.
- **ScreenPorch:** Screen porch area in square feet.
- **PoolArea:** Pool area in square feet.
- **PoolQC:** Pool quality.
- **Fence:** Fence quality.
- **MiscFeature:** Miscellaneous feature not covered in other categories.
- **MiscVal:** Dollar value of miscellaneous features.
- **MoSold:** Month Sold.
- **YrSold:** Year Sold.
- **SaleType:** Type of sale.
- **SaleCondition:** Condition of sale.

## Project Structure  
machine_learning_project_Ames_House_Price/
│
├── data/                     # Dataset and data processing scripts
│   └── ames.csv         # Ames housing dataset
│
├── notebooks/                # Jupyter notebooks for EDA and modeling
│   ├── 01_EDA.ipynb          # Exploratory Data Analysis
│   └── 02_Modeling.ipynb     # Machine learning models
│
├── models/                   # Saved machine learning models
│   ├── linear_regression.pkl
│   └── random_forest.pkl
│
├── src/                      # Source code for data processing and modeling
│   ├── data_preprocessing.py # Data cleaning and feature engineering
│   └── model_training.py     # Model training and evaluation
│
├── results/                  # Analysis results and model performance metrics
│   └── model_comparison.png
│
└── README.md                 # Project overview and documentation


## Technologies Used  
- **Python**: Programming language for data analysis and machine learning.  
- **Pandas**: Data manipulation and analysis.  
- **NumPy**: Numerical computing.  
- **Matplotlib & Seaborn**: Data visualization.  
- **Scikit-learn**: Machine learning models and evaluation metrics.  
- **Jupyter Notebook**: Interactive data analysis and model development environment.  

## Machine Learning Models Implemented  
- **Linear Regression**: To model the relationship between features and insurance charges.  
- **Random Forest Regressor**: An ensemble learning method to improve prediction accuracy.  
- **Gradient Boosting Regressor**: To capture complex patterns in the data.  

## Results and Insights  
- **Linear Regression** provided a baseline performance with an R² score of X.  
- **Random Forest Regressor** outperformed other models with an R² score of Y, indicating better predictive power.  
- **Gradient Boosting Regressor** showed competitive performance with high accuracy and generalization.  
- Key features influencing insurance charges included **BMI**, **age**, and **smoking status**.  

## Installation and Usage  
1. Clone the repository:  
    ```bash
    git clone https://github.com/your-username/machine_learning_project_Ames_House_Price.git
    cd machine_learning_project_Ames_House_Price
    ```  
2. Install the required dependencies:  
    ```bash
    pip install -r requirements.txt
    ```  
3. Run the Jupyter notebooks to explore the data and train models:  
    ```bash
    jupyter notebook
    ```  

## How to Contribute  
Contributions are welcome! Feel free to open issues, submit pull requests, or suggest enhancements.  
1. Fork the repository.  
2. Create your feature branch: `git checkout -b feature/YourFeatureName`.  
3. Commit your changes: `git commit -m 'Add some feature'`.  
4. Push to the branch: `git push origin feature/YourFeatureName`.  
5. Open a pull request.  

## License  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  

## Acknowledgments  
- The dataset used in this project is publicly available from [source of the dataset].  
- Special thanks to the open-source community for the tools and libraries used in this project.  

## Contact  
For any inquiries, feel free to reach out:  
- GitHub: [waheb-1988](https://github.com/your-username)  
- Email: [hocineabdelouaheb@yahoo.fr]  
