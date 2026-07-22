from collections import defaultdict

class PortScanDetector:

    def __init__(self):
        self.port_history = defaultdict(set)

    def analyze(self, src_ip, dst_port):

        self.port_history[src_ip].add(dst_port)

        if len(self.port_history[src_ip]) > 20:

            return {
                "threat": "Port Scan",
                "score": 80
            }

        return None