🩺 Diabetes Detection Using Machine Learning
🔍 Project Overview
This project predicts the onset of diabetes based on diagnostic medical measurements using machine learning classification techniques. By analyzing patient health metrics—such as glucose levels, insulin, BMI, and age—the model assists in early risk assessment and data-driven healthcare decisions.

📁 Dataset
Typically based on the standard Pima Indians Diabetes Dataset.

Features:

Pregnancies: Number of times pregnant

Glucose: Plasma glucose concentration (2 hours in an oral glucose tolerance test)   

BloodPressure: Diastolic blood pressure (mm Hg)   

SkinThickness: Triceps skin fold thickness (mm)   

Insulin: 2-Hour serum insulin (mu U/ml)   

BMI: Body mass index (weight in kg / (height in m)²)   

DiabetesPedigreeFunction: Diabetes genetic history score

Age: Age in years

Target:

Outcome: Class variable (0 = Non-Diabetic, 1 = Diabetic)

🛠️ Technologies Used
Python

Pandas (Data manipulation and cleaning)

NumPy (Numerical operations)

Matplotlib  (Data visualization )

Scikit-learn (Model building, preprocessing, and evaluation)

⚙️ Workflow
Load and Inspect Data: Check data distributions and identify non-physiological zero values (e.g., zero glucose, blood pressure, or BMI).

Data Preprocessing: Handle missing/zero values via imputation (median/mean) and apply feature scaling (StandardScaler).

Exploratory Data Analysis (EDA): Analyze feature correlations, class balance, and distribution plots.

Model Training: Train supervised classification models (Logistic Regression, Random Forest, or Support Vector Machines).

Model Evaluation: Evaluate performance using:

Accuracy Score




📈 Results & Insights
Glucose Level & BMI: Exhibit the strongest positive correlation with a diabetic diagnosis.

Age: Shows moderate risk correlation, particularly when combined with high BMI.

Recall / Sensitivity: Prioritized during evaluation to minimize false negatives (failing to identify an at-risk patient).

🎯 Purpose
Understand the influence of clinical diagnostic indicators on diabetes onset.

Practice binary classification, data imputation, and medical risk metric evaluation.

Build a clean, reproducible healthcare machine learning portfolio project.
