# 🏏 IPL First-Innings Score Prediction Using Machine Learning

## 📌 Project Overview

The **IPL First-Innings Score Prediction** project uses Machine Learning to predict the final first-innings score of an IPL match based on the match situation after 10 overs.

The model analyzes factors such as batting team, bowling team, venue, runs scored, wickets lost and recent scoring performance to estimate the final score.

An interactive web application was developed using **Streamlit**, allowing users to enter match details and receive a predicted score.

## 🎯 Objectives

* Analyze historical IPL ball-by-ball match data.
* Perform data cleaning and preprocessing.
* Explore relationships between match statistics and final scores.
* Train and compare multiple Machine Learning regression models.
* Tune the Random Forest model using GridSearchCV.
* Develop an interactive web application for score prediction.

## 📂 Dataset

The project uses historical IPL ball-by-ball match data.

* **Total matches in original dataset:** 617
* **Total ball-by-ball records:** 76,014
* **Matches used for modeling:** 616
* **Prediction point:** After 10 completed overs
* **Target variable:** Final first-innings score (`total`)

One match that did not reach 10 overs was excluded from the modeling dataset.

link:  https://www.kaggle.com/yuvrajdagur/ipl-dataset-season-2008-to-2017.

### Features Used

| Feature        | Description                        |
| -------------- | ---------------------------------- |
| batting_team   | Team batting first                 |
| bowling_team   | Team bowling first                 |
| venue          | Match venue                        |
| runs           | Runs scored after 10 overs         |
| wickets        | Wickets lost after 10 overs        |
| runs_last_5    | Runs scored in the last 5 overs    |
| wickets_last_5 | Wickets lost in the last 5 overs   |
| total          | Final first-innings score (target) |

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook

## ⚙️ Project Workflow

1. **Data Loading:** Loaded the IPL ball-by-ball dataset using Pandas.
2. **Data Cleaning:** Standardized team names and checked the dataset for missing values.
3. **Feature Engineering:** Converted cricket over notation into completed balls and identified the match situation after 10 overs.
4. **Data Preparation:** Created one record per match using the match information available after 10 completed overs.
5. **Exploratory Data Analysis:** Analyzed score distributions, relationships between runs and final scores, and feature correlations.
6. **Train-Test Split:** Split the data into 80% training and 20% testing sets.
7. **Preprocessing:** Applied One-Hot Encoding to categorical features using `ColumnTransformer`.
8. **Model Training:** Trained and compared four regression models.
9. **Hyperparameter Tuning:** Used GridSearchCV with 5-fold cross-validation to tune Random Forest.
10. **Evaluation:** Evaluated the final model using MAE, RMSE and R².
11. **Deployment:** Saved the trained pipeline using Joblib and developed an interactive Streamlit application.

## 📊 Exploratory Data Analysis

The following analyses were performed:

* Distribution of final first-innings scores.
* Relationship between runs scored after 10 overs and final scores.
* Correlation between match statistics and final scores.

The analysis showed that runs scored after 10 overs had a positive relationship with the final score, while wickets lost had a negative relationship.

## 🤖 Machine Learning Models

The following regression models were trained and compared:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor

### Model Comparison

| Model             |   MAE |  RMSE |    R² |
| ----------------- | ----: | ----: | ----: |
| Linear Regression | 15.69 | 19.45 | 0.511 |
| Decision Tree     | 17.87 | 23.46 | 0.289 |
| Random Forest     | 15.13 | 19.25 | 0.521 |
| Gradient Boosting | 15.61 | 19.95 | 0.486 |

## 🔍 Hyperparameter Tuning

GridSearchCV with 5-fold cross-validation was used to tune the Random Forest Regressor.

**Best parameters:**

* `n_estimators`: 200
* `max_depth`: 8
* `min_samples_split`: 2

**Best cross-validation RMSE:** 20.81

## 📈 Final Model Evaluation

The tuned Random Forest model was evaluated on the held-out test dataset.

| Metric                         | Result |
| ------------------------------ | -----: |
| Mean Absolute Error (MAE)      |  15.17 |
| Root Mean Squared Error (RMSE) |  19.21 |
| R² Score                       |  0.524 |

The model achieved an MAE of approximately 15.17 runs on the test dataset. The R² score indicates that the model explains approximately 52.4% of the variation in final scores in this test set.

## 🌐 Streamlit Web Application

An interactive Streamlit application was developed to make score prediction easy.

Users can enter:

* Batting team
* Bowling team
* Venue
* Runs after 10 overs
* Wickets lost
* Runs in the last 5 overs
* Wickets lost in the last 5 overs

The application uses the saved Random Forest pipeline to predict the final first-innings score.

### Application Screenshot



## 📁 Project Structure

```text
IPL-Score-Prediction/
│
├── IPL_Score_Prediction.ipynb
├── ipl_app.py
├── ipl_score_prediction_model.pkl
├── requirements.txt
└── README.md
```

## 🚀 How to Run the Project

### 1. Clone the Repository

git clone https://github.com/Dhanusri-analyst/-IPL-First-Innings-Score-Prediction-Using-Machine-Learning.git

### 2. Navigate to the Project Folder

-IPL-First-Innings-Score-Prediction-Using-Machine-Learning

### 3. Install the Required Libraries

pip install -r IPL requirements.txt


### 4. Run the Streamlit Application

streamlit run ipl_app.py

### 5. Open the Application

Open the local URL displayed in your terminal, usually:


http://localhost:8501

## ⚠️ Limitations

* The model uses historical IPL data and may not represent current team compositions or playing conditions.
* Predictions are based on match information available after 10 completed overs.
* The model does not include player-specific information.
* Predictions are estimates and may differ from actual match scores.

## 🔮 Future Improvements

* Include more recent IPL seasons.
* Add player-level statistics and other match conditions.
* Experiment with additional regression algorithms.
* Improve prediction performance through feature engineering.
* Deploy the application online for public access.

## 👩‍💻 Author

**Dhanusri Prabhakaran**

https://www.linkedin.com/in/dhanusri-prabhakaran-19106b329

https://github.com/Dhanusri-analyst


⭐ If you find this project interesting, feel free to explore the repository.
