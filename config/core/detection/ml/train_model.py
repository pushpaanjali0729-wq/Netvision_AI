import joblib
import pandas as pd

from sklearn.ensemble import (
    IsolationForest
)

from sklearn.svm import (
    OneClassSVM
)

df = pd.read_csv(
    "data/traffic.csv"
)

X = df[["packet_length"]]

iso = IsolationForest(
    contamination=0.05
)

iso.fit(X)

svm = OneClassSVM()

svm.fit(X)

joblib.dump(
    iso,
    "models/isolation_forest.pkl"
)

joblib.dump(
    svm,
    "models/oneclass_svm.pkl"
)

print("Models Trained")