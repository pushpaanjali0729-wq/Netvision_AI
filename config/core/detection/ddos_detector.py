from collections import defaultdict
from time import time

class DDoSDetector:

    def __init__(self):

        self.packet_counter = defaultdict(list)

    def analyze(self, src_ip):

        current_time = time()

        self.packet_counter[src_ip].append(
            current_time
        )

        self.packet_counter[src_ip] = [

            t for t in self.packet_counter[src_ip]

            if current_time - t < 1
        ]

        if len(self.packet_counter[src_ip]) > 100:

            return {

                "threat": "Potential DDoS",

                "score": 90
            }

        return None