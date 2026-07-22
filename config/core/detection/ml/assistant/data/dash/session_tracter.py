# core/session_tracker.py

from collections import defaultdict


class SessionTracker:

    def __init__(self):

        self.sessions = defaultdict(int)

    def add_connection(
            self,
            src_ip,
            dst_ip
    ):

        key = (
            src_ip,
            dst_ip
        )

        self.sessions[key] += 1

    def total_sessions(self):

        return len(
            self.sessions
        )