# core/flow_tracker.py

from collections import defaultdict


class FlowTracker:

    def __init__(self):

        self.bytes_sent = defaultdict(int)

    def update(
            self,
            src_ip,
            packet_length
    ):

        self.bytes_sent[
            src_ip
        ] += packet_length

    def top_talkers(self):

        return sorted(

            self.bytes_sent.items(),

            key=lambda x: x[1],

            reverse=True
        )[:10]