import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load data
data = pd.read_csv("filtered.csv")

# Separate features and target
X = data.drop('treatment', axis=1)
y = data['treatment']

# Encode target
le = LabelEncoder()
y_encoded = le.fit_transform(y)


gender_cols = ['Female', 'Male', 'Other']
self_employed_cols = ['No', 'Yes']
family_history_cols = ['No', 'Yes']
work_interfere_cols = ['Never', 'Rarely', 'Sometimes', 'Often']
no_employees_cols = ['1-5', '6-25', '26-100', '100-500', '500-1000', 'More than 1000']
remote_work_cols = ['No', 'Yes']
tech_company_cols = ['No', 'Yes']
benefits_cols = ['No', "Don't know", 'Yes']
care_options_cols = ['No', 'Not sure', 'Yes']
wellness_program_cols = ['No', "Don't know", 'Yes']
seek_help_cols = ['No', "Don't know", 'Yes']
anonymity_cols = ['No', "Don't know", 'Yes']
leave_cols = ['Very easy', 'Somewhat easy', "Don't know", 'Somewhat difficult', 'Very difficult']
mental_health_consequence_cols = ['No', 'Maybe', 'Yes']
phys_health_consequence_cols = ['No', 'Maybe', 'Yes']
coworkers_col = ['No', 'Some of them', 'Yes']
supervisor_cols = ['No', 'Some of them', 'Yes']
mental_health_interview_cols = ['No', 'Maybe', 'Yes']
phys_health_interview_cols = ['No', 'Maybe', 'Yes']
mental_vs_physical_cols = ["Don't know", 'No', 'Yes']
obs_consequence_cols = ['No', 'Yes']

# Combine all categorical columns
columns_for_encoder = [gender_cols, self_employed_cols, family_history_cols, work_interfere_cols,
                    no_employees_cols, remote_work_cols, tech_company_cols, benefits_cols,
                    care_options_cols, wellness_program_cols, seek_help_cols, anonymity_cols,
                    leave_cols, mental_health_consequence_cols, phys_health_consequence_cols,
                    coworkers_col, supervisor_cols, mental_health_interview_cols,
                    phys_health_interview_cols, mental_vs_physical_cols, obs_consequence_cols]




features = list(X.columns)
print(features)
print(data['leave'].unique())

ord_encoder = OrdinalEncoder(categories=list(columns_for_encoder))
print("Before fit_transform")
X[features[1:]] = ord_encoder.fit_transform(X.iloc[:,1:])

print("After fit_transform")
# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.33, random_state=42)

print('Divided')


# Initialize and train classifier
classifier = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
print('Classifier Taken')
classifier.fit(X_train, y_train)

# Predict and evaluate the model
y_pred = classifier.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Save model and encoder
pickle.dump(classifier, open("model.pkl", "wb"))
pickle.dump(ord_encoder, open("ord_encoder.pkl", "wb"))