import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression, RidgeClassifier, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import classification_report

mush = pd.read_csv("mushrooms.csv")

mush.head()

classes = mush["class"].value_counts()
print(classes)

plt.bar("Edible", classes["e"])
plt.bar("Poisonous", classes["p"])
plt.show()


X = mush.loc[:, ["cap-shape", "cap-color", "ring-number", "ring-type"]]
y = mush.loc[:, "class"]

# Encoding the columns

for i in X.columns:
    X[i] = LabelEncoder().fit_transform(X[i])

y = LabelEncoder().fit_transform(y)

print(X)
print(y)

# train test split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Models

logistic_reg = LogisticRegression()
ridge_reg = RidgeClassifier()
decision_tree = DecisionTreeClassifier()
naive_bayes = GaussianNB()
neural_network = MLPClassifier()

# training

models = [logistic_reg, ridge_reg,
          decision_tree, naive_bayes,
          neural_network]

for model in models:
    model.fit(X_train, y_train)

# predictions

models = [
    ('Logistic Regression', logistic_reg),
    ('Ridge Regression', ridge_reg),
    ('Decision Tree', decision_tree),
    ('Naive Bayes', naive_bayes),
    ('Neural Network', neural_network)
]

predictions = {}

for model_name, model in models:
    predictions[model_name] = model.predict(X_test)


reports = [
    ('Logistic Regression', predictions['Logistic Regression']),
    ('Ridge Regression', predictions['Ridge Regression']),
    ('Decision Tree', predictions['Decision Tree']),
    ('Naive Bayes', predictions['Naive Bayes']),
    ('Neural Network', predictions['Neural Network'])
]

for model_name, y_pred in reports:
    report = classification_report(y_test, y_pred)
    print(f"{model_name}:\n{report}")

# Decision Tree works best with 91% accuracy.
