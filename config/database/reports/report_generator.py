# reports/report_generator.py

from datetime import datetime

from reports.pdf_report import (
    PDFReport
)


class ReportGenerator:

    def create_daily_report(
            self,
            total_packets,
            anomalies,
            suspicious_ips
    ):

        data = {

            "Date":
                datetime.now(),

            "Packets":
                total_packets,

            "Anomalies":
                anomalies,

            "Suspicious IPs":
                suspicious_ips
        }

        report = PDFReport()

        report.generate(
            "reports/daily_report.pdf",
            data
        )