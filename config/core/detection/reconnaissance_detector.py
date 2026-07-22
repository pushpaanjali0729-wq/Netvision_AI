# detection/reconnaissance_detector.py

from collections import defaultdict


class ReconnaissanceDetector:

    def __init__(self):

        self.targets = defaultdict(set)

    def analyze(
            self,
            src_ip,
            dst_ip
    ):

        self.targets[src_ip].add(
            dst_ip
        )

        if len(
            self.targets[src_ip]
        ) > 20:

            return {

                "threat": "Network Reconnaissance",

                "score": 80
            }

        return None