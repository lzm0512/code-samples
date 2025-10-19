# Setup
!pip install pandas scikit-learn matplotlib seaborn --quiet

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from google.colab import files
uploaded = files.upload()
df = pd.read_csv("penguins_lter.csv")

# Cleaning the data
# Keep only columns containing useful data, deleting columns containing NaN terms
useful_columns = ["Species", "Island", "Culmen Length (mm)", "Culmen Depth (mm)",
                  "Flipper Length (mm)", "Body Mass (g)", "Sex"]
df = df[useful_columns].dropna()

# Encoding categorical variables
LE_labels = {}
for col in ["Island", "Sex"]:
  LE = LabelEncoder()
  df[col] = LE.fit_transform(df[col])
  LE_labels[col] = LE

# Extract Species
x = df.drop("Species", axis=1)
y = df["Species"]

# Encoding Species
LE_species = LabelEncoder()
y = LE_species.fit_transform(y)

# Splitting data into training and testing
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size = 0.2, random_state = 42, stratify = y)

# Scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Training
model = RandomForestClassifier(random_state=42)
model.fit(x_train, y_train)

# Evaluate
y_pred = model.predict(x_test)

print("\nAccuracy:", round(accuracy_score(y_test, y_pred), 3))
print("\nClassification report:")
print(classification_report(y_test, y_pred, target_names=LE_species.classes_))

# Confusion matrix
m_confusion = confusion_matrix(y_test, y_pred)
sns.heatmap(
    m_confusion, annot=True, fmt='d', cmap='Greys',
    xticklabels=LE_species.classes_,
    yticklabels=LE_species.classes_
)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Feature importance
importances = pd.Series(model.feature_importances_, index=x.columns)
importances.sort_values().plot(kind='barh', color='grey')
plt.title("Feature Importance in Penguin Species Classification")
plt.xlabel("Importance")
plt.show()
