# 🏡 Ridge Regression – Predicting House Prices

## 📌 Project Overview
This project focuses on predicting house prices using **regression techniques**.  
We build and compare **Ordinary Least Squares (OLS)** and **Ridge Regression** models to evaluate which performs better in the presence of **multicollinearity** among features.

- **Dataset:** [House Prices Dataset](https://drive.google.com/file/d/1FDbOghfF0PbG7F8T1TNjK2U9c0BzDZTJ/view?usp=sharing)  
- **Features:**  
  - `size_m2` – size of the house in square meters  
  - `bedrooms` – number of bedrooms  
  - `bathrooms` – number of bathrooms  
  - `distance_city` – distance from the city center (km)  
  - `age_years` – age of the property in years  

- **Target Variable:**  
  - `price_k` – house price (in thousands)

---

## 🎯 Problem Statement
A **real-estate agency** wants to estimate house prices for potential buyers and sellers.  
However, the dataset contains **highly correlated features** (`size_m2` and `bedrooms`).  
This can lead to **unstable OLS coefficients** and poor generalization.  

To overcome this, we apply **Ridge Regression**, which adds an L2 penalty to stabilize coefficient estimates.

---

## ⚙️ Methodology

1. **Exploratory Data Analysis (EDA)**  
   - Checked correlations between features  
   - Identified multicollinearity problem (`size_m2` ↔ `bedrooms`)

2. **Modeling Approaches**  
   - **OLS Regression (Baseline)**: Fits coefficients without penalty  
   - **Ridge Regression**: Penalizes large coefficients to reduce overfitting and handle collinearity

3. **Model Evaluation**  
   - Compared coefficients from OLS vs Ridge  
   - Evaluated on **R² score** (goodness of fit)  
   - Analyzed performance on **test data**

---

## 📊 Results

- **OLS Regression**
  - Coefficients were unstable due to multicollinearity  
  - R² (test): Lower, indicating poor generalization  

- **Ridge Regression**
  - Coefficients were **shrunken and more stable**  
  - R² (test): Higher, better generalization to unseen data  

---

## ✅ Why Ridge Regression is Better Here
- **OLS Problem:** With highly correlated predictors, OLS assigns exaggerated and unstable coefficients, even if predictive power is low.  
- **Ridge Solution:** By introducing an **L2 penalty**, Ridge shrinks coefficients of correlated variables together, improving:
  - **Stability of coefficients**  
  - **Model interpretability**  
  - **Generalization performance**  

Thus, **Ridge Regression is preferred when predictors are correlated**, as in this real-estate dataset.

---

## 📌 Tech Stack
- Python  
- NumPy, Pandas  
- Scikit-learn (OLS & Ridge regression, evaluation metrics)  

---
📈 Future Improvements

Try Lasso Regression for feature selection

Experiment with RidgeCV (automatic alpha tuning)

Build a web app for interactive house price prediction

# House-price-prediction-end-to-end-project
