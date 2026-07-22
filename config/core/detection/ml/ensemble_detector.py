import joblib


class EnsembleDetector:

    def __init__(self):

        self.iso = joblib.load(
            "models/isolation_forest.pkl"
        )

        self.svm = joblib.load(
            "models/oneclass_svm.pkl"
        )

    def predict(self, packet_length):

        value = [[packet_length]]

        iso_pred = self.iso.predict(value)

        svm_pred = self.svm.predict(value)

        score = 0

        if iso_pred[0] == -1:
            score += 50

        if svm_pred[0] == -1:
            score += 50

        return score