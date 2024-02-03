import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

df = pd.read_csv('university_data.csv')

df.describe()

df.head

# Assuming your dataset is stored in a CSV file named 'university_data.csv'
# Replace 'university_data.csv' with the actual file path if needed
df = pd.read_csv('university_data.csv')


# Data Preprocessing
# Split data into features (X) and target variable (y)
X = df.drop(['University Name', 'Admit Probability'], axis=1)
y_actual = df['University Name']

# Convert to binary classification based on a threshold (e.g., 0.8)
threshold = 0.8
y_binary = (df['Admit Probability'] >= threshold).astype(int)

# Define numerical and categorical features
numerical_features = ['GRE Score', 'GPA', 'IELTS Score', 'University Ranking']
categorical_features = []  # Since 'Research Experience' is dropped

# Create transformers for numerical and categorical features
numerical_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(drop='first', sparse=False)

# Create a column transformer to apply different transformers to different columns
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test_actual, y_train_binary, y_test_binary = train_test_split(
    X, y_actual, y_binary, test_size=0.2, random_state=42
)

# Create a pipeline with RandomForestClassifier
rf_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))  # Adjust parameters as needed
])

# Create a pipeline with XGBoost
xgb_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', XGBClassifier(random_state=42))  # Adjust parameters as needed
])

# Create a pipeline with CatBoost
catboost_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', CatBoostClassifier(random_state=42, verbose=0))  # Adjust parameters as needed
])

# Train and evaluate RandomForestClassifier
rf_pipeline.fit(X_train, y_train_binary)
y_pred_rf = rf_pipeline.predict(X_test)
accuracy_rf = accuracy_score(y_test_binary, y_pred_rf)
conf_matrix_rf = confusion_matrix(y_test_binary, y_pred_rf)

print("RandomForestClassifier:")
print(f'Accuracy: {accuracy_rf}')
print('Confusion Matrix:')
print(conf_matrix_rf)

# Train and evaluate XGBoost
xgb_pipeline.fit(X_train, y_train_binary)
y_pred_xgb = xgb_pipeline.predict(X_test)
accuracy_xgb = accuracy_score(y_test_binary, y_pred_xgb)
conf_matrix_xgb = confusion_matrix(y_test_binary, y_pred_xgb)

print("\nXGBoost:")
print(f'Accuracy: {accuracy_xgb}')
print('Confusion Matrix:')
print(conf_matrix_xgb)

# Train and evaluate CatBoost
catboost_pipeline.fit(X_train, y_train_binary)
y_pred_catboost = catboost_pipeline.predict(X_test)
accuracy_catboost = accuracy_score(y_test_binary, y_pred_catboost)
conf_matrix_catboost = confusion_matrix(y_test_binary, y_pred_catboost)

print("\nCatBoost:")
print(f'Accuracy: {accuracy_catboost}')
print('Confusion Matrix:')
print(conf_matrix_catboost)



# Assuming your dataset is stored in a CSV file named 'university_data1.csv'
# Replace 'university_data.csv' with the actual file path if needed
df = pd.read_csv('university_data.csv')

# Data Exploration and Visualization

# Exclude non-numeric columns before creating the correlation heatmap
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
correlation_df = df[numeric_columns]

# Pairplot for numerical features
sns.pairplot(df, hue='Research Paper', palette='viridis')
plt.title('Pairplot of Numerical Features')
plt.show()

# Boxplot for University Ranking
plt.figure(figsize=(10, 6))
sns.boxplot(x='University Ranking', y='Admit Probability', data=df)
plt.title('Boxplot of University Ranking vs. Admit Probability')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_df.corr(), annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()

# Countplot for Research Experience
plt.figure(figsize=(8, 5))
sns.countplot(x='Research Paper', data=df)
plt.title('Countplot of Research Paper')
plt.show() 