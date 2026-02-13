import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("kidney_disease.csv")

X = df.drop(columns=["classification"])

y = df["classification"]

# random_state is fixed to ensure reproducible results
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Training set size is:", X_train.shape)
print("Testing set size is:", X_test.shape)


# same data should not be used to train and test a model
# because the model may simply memorize the data instead
# of learning general patterns, leading to misleading results.
# The testing set is used to evaluate how well the model performs on new, unseen data.
# This helps us understand whether the model can generalize beyond the data it was trained on.
