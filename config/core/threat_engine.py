from detection.port_scan_detector import (
    PortScanDetector
)

from detection.ddos_detector import (
    DDoSDetector
)

from detection.dns_anomaly_detector import (
    DNSAnomalyDetector
)

from detection.blacklist_detector import (
    BlacklistDetector
)


class ThreatEngine:

    def __init__(self):

        self.port_scan = PortScanDetector()

        self.ddos = DDoSDetector()

        self.dns = DNSAnomalyDetector()

        self.blacklist = BlacklistDetector()

    def analyze(
            self,
            src_ip,
            dst_port=None,
            dns_query=None
    ):

        alerts = []

        result = self.ddos.analyze(src_ip)

        if result:
            alerts.append(result)

        result = self.blacklist.analyze(src_ip)

        if result:
            alerts.append(result)

        if dst_port:

            result = self.port_scan.analyze(
                src_ip,
                dst_port
            )

            if result:
                alerts.append(result)

        if dns_query:

            result = self.dns.analyze(
                dns_query
            )

            if result:
                alerts.append(result)

        return alerts