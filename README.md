# HousePredict :

![License: Non-Commercial Use Only](https://img.shields.io/badge/license-Non--Commercial-orange)

This project is a machine learning web application that predicts the median house price in California districts based on user inputs. It leverages linear regression and feature engineering to give accurate predictions, with a user-friendly frontend built using HTML, CSS, and JavaScript, and a backend powered by Flask.

# Features:
- Predicts house prices based on demographic and location data.
- Trained on the California Housing Dataset.
- Feature engineering for improved model performance.
- Web interface for user input and result visualization.
- Sample house gallery for UI enhancement.


# Technologies Used:
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **ML Libraries:** Scikit-learn, Pandas, NumPy, Joblib
- **Visualization:** Matplotlib, Seaborn

# Features Used in the Model:
- longitude, latitude
- housing_median_age
- total_rooms, total_bedrooms
- population, households
- median_income
- **Engineered Features:**
  - bedroom_ratio = total_bedrooms / total_rooms
  - household_rooms = total_rooms / households
- **Categorical location types (one-hot encoded):**
  - <1H OCEAN, INLAND, ISLAND, NEAR BAY, NEAR OCEAN

# Model Overview:
The model is trained using **Linear Regression** with mean squared error as the evaluation metric. Data was preprocessed using normalization, missing value handling, and categorical encoding.

# Contributing:
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

This project is licensed for personal and educational use only.  
Commercial use is not allowed.  
See the [LICENSE](./LICENSE) file for full terms.
