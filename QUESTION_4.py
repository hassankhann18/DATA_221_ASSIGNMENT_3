import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv("kidney_disease.csv")

y = df["classification"].map({"ckd": 0, "notckd": 1})

X = df.drop(columns=["classification"]).apply(pd.to_numeric, errors="coerce")

data = X.copy()
data["classification"] = y
data = data.dropna()

y = data["classification"].astype(int)
X = data.drop(columns=["classification"])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# KNN (k=5)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict
y_predict = knn.predict(X_test)

# Confusion matrix + accuracy
cm = confusion_matrix(y_test, y_predict)
acc = accuracy_score(y_test, y_predict)

print("Confusion Matrix:")
print(cm)
print("\nAccuracy:", acc)



# A True Positive occurs when the model correctly predicts kidney disease.
# A True Negative occurs when the model correctly predicts no kidney disease.
# A False Positive occurs when the model predicts kidney disease incorrectly.
# A False Negative occurs when the model fails to detect kidney disease.
# Accuracy alone may not fully reflect how serious the model’s errors are.
