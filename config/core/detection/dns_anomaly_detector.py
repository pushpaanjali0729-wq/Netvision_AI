class DNSAnomalyDetector:

    def analyze(self, query_name):

        if not query_name:
            return None

        if len(query_name) > 50:

            return {

                "threat": "Suspicious DNS Query",

                "score": 70
            }

        return None