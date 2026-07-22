# ml/explainability.py


class ExplainabilityEngine:

    def explain(
            self,
            packet_length,
            threat_score
    ):

        explanation = []

        if packet_length > 1500:

            explanation.append(
                "Large packet size detected"
            )

        if threat_score > 80:

            explanation.append(
                "High anomaly confidence"
            )

        return explanation