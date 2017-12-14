import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score
from sklearn.model_selection import train_test_split
np.random.seed(42)

df = pd.read_csv('./admissions.csv')
df.head()

df[['p1', 'p2', 'p3', 'p4']] = pd.get_dummies(df['prestige'])
df.head()

y = df['admit']
X = df[['gre', 'gpa', 'p1', 'p2', 'p3']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=0)

mod = LogisticRegression()
mod.fit(X_train, y_train)
y_predicts = mod.predict(X_test)

print(precision_score(y_test, y_predicts))
print(recall_score(y_test, y_predicts))
print(accuracy_score(y_test, y_predicts))
confusion_matrix(y_test, y_predicts)