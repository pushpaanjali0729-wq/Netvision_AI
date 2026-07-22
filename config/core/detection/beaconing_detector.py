# detection/beaconing_detector.py

from collections import defaultdict


class BeaconingDetector:

    def __init__(self):

        self.connection_times = defaultdict(list)

    def analyze(
            self,
            src_ip,
            timestamp
    ):

        self.connection_times[src_ip].append(
            timestamp
        )

        if len(
            self.connection_times[src_ip]
        ) >= 5:

            return {

                "threat": "Beaconing Activity",

                "score": 75
            }

        return None