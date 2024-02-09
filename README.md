# University Recommendation System
This repository contains two Jupyter notebooks: usrecomm.ipynb and canadarecomm.ipynb, implementing a University Recommendation System for students seeking admission to universities in the United States and Canada.

## Files and Structure
usrecomm.ipynb: Jupyter notebook for the University Recommendation System based on user input for the United States.
canadarecomm.ipynb: Jupyter notebook for the University Recommendation System based on user input for Canada.
university_data1.csv and university_data.csv : Dataset containing information about universities for training and testing the recommendation models.

## Requirements
Make sure you have the following dependencies installed:

- pandas
- matplotlib
- seaborn
- scikit-learn
- xgboost
- catboost

You can install them using the following command:
## pip install pandas matplotlib seaborn scikit-learn xgboost catboost

## How to Use
Open the respective Jupyter notebook (usrecomm.ipynb or canadarecomm.ipynb).
Run the notebook cells sequentially.
Input the required information when prompted (e.g., GRE Score, IELTS Score, University Ranking, etc.).
The system will recommend universities based on the provided information.

## Data Exploration
The notebooks include data exploration and visualization using pair plots, box plots, and correlation heatmaps to gain insights into the relationships between different features.

## Model Evaluation
The recommendation models are evaluated using accuracy scores and confusion matrices. Different classifiers like RandomForest, XGBoost, and CatBoost are employed to provide a comprehensive comparison.

### accuracy for usrecomm : 74% -- using catboost | 74% -- using randomforest | 72% -- using xgboost

###  accuracy for canadarecomm : 83% -- using catboost | 80% -- using randomforest | 77% -- using xgboost

Feel free to explore, modify, and experiment with the code to adapt it to your specific use case.

