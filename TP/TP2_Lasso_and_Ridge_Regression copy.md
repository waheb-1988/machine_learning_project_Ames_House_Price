# TP2: Lasso and Ridge Regression  
This second TP **Lasso** and **Ridge Regression** using the **Ames Housing Dataset**. These regularization techniques address overfitting and improve model generalization.  

---

## 1. Recap of Linear Regression  
### Objective  
Review key concepts from TP1 to build a foundation for regularization.  

### Activities  
- Quick review of Linear Regression and its limitations (e.g., overfitting).  
- Discuss how high multicollinearity and complex models can lead to overfitting.  
- Introduce the need for regularization to penalize complex models.  

---

## 2. Introduction to Regularization  
### Objective  
Understand the purpose and mechanics of Lasso and Ridge regression.  

### Concepts Covered  
- **Ridge Regression (L2 Regularization)**: Penalizes large coefficients to reduce model complexity.  
- **Lasso Regression (L1 Regularization)**: Performs feature selection by shrinking some coefficients to zero.  
- Mathematical formulation and cost functions for both methods.  

---

## 3. Data Preparation  
### Objective  
Prepare the Ames Housing data for Lasso and Ridge regression.  

### Activities  (from TP1)
- Load the dataset using `pandas`.  
- Perform data cleaning and preprocessing .  
- Encode categorical variables using `OneHotEncoder()` or `pd.get_dummies()`.  
- Split the data using `train_test_split()` with an 80/20 ratio.  
- Apply `StandardScaler()` to standardize numerical features.  

---

## 4. Ridge Regression  
### Objective  
Implement Ridge Regression and understand its impact on overfitting.  

### Activities  
- Train a Ridge Regression model using `Ridge()` from `scikit-learn`.  
- Perform hyperparameter tuning for the regularization strength (`alpha`) using `GridSearchCV`.  
- Evaluate model performance using `MAE`, `MSE`, and `R2 Score`.  
- Visualize coefficient magnitudes to understand regularization effects.  

### Exercise:  
- Experiment with different values of `alpha` and observe its impact on model complexity and performance.  
- Compare Ridge performance with the Linear Regression model from TP1.  

---

## 5. Lasso Regression  
### Objective  
Explore Lasso Regression and its feature selection capability.  

### Activities  
- Train a Lasso Regression model using `Lasso()` from `scikit-learn`.  
- Perform hyperparameter tuning for `alpha` using `GridSearchCV`.  
- Evaluate model performance using `MAE`, `MSE`, and `R2 Score`.  
- Visualize how Lasso shrinks some coefficients to zero, effectively performing feature selection.  

### Exercise:  
- Experiment with different `alpha` values and observe which features are retained.  
- Compare Lasso performance with Ridge and Linear Regression models.  

---

## 6. Comparison and Interpretation  
### Objective  
Compare the performance of Linear, Ridge, and Lasso regression models.  

### Activities  
- Compare performance metrics (`MAE`, `MSE`, `R2 Score`) for all three models.  
- Discuss the trade-offs between bias and variance with different regularization strengths.  
- Highlight scenarios where Lasso (feature selection) or Ridge (multicollinearity) is more appropriate.  

### Exercise:  
- Plot the coefficients of all models to compare feature importance.  
- Analyze and interpret which features are most influential in predicting `SalePrice`.  

---

## 7. Cross-Validation and Model Tuning  
### Objective  
Ensure robust model evaluation and fine-tuning.  

### Activities  
- Use `cross_val_score()` to perform cross-validation for each model.  
- Fine-tune hyperparameters for Ridge and Lasso using `GridSearchCV`.  
- Discuss the importance of cross-validation in model selection.  

### Exercise:  
- Implement cross-validation for Ridge and Lasso models.  
- Analyze the effect of cross-validation on model stability and generalization.  

---

## 8. Conclusion and Next Steps  
### Objective  
Summarize key takeaways and suggest next steps for further learning.  

### Activities  
- Recap the strengths and limitations of Ridge and Lasso Regression.  
- Discuss alternative regularization techniques like ElasticNet.  
- Suggest exploring non-linear models like Decision Trees or Ensemble methods.  

---

## Optional Advanced Exercise: ElasticNet  
- Introduce ElasticNet, which combines L1 and L2 penalties.  
- Implement `ElasticNet()` from `scikit-learn` and compare it with Ridge and Lasso.  

---

Happy Learning! 🚀
