# reports/executive_report.py

from reports.pdf_report import PDFReport


class ExecutiveReport:

    def generate(
        self,
        packets,
        threats,
        health
    ):

        report = PDFReport()

        data = {

            "Total Packets": packets,

            "Threats Detected": threats,

            "Network Health": f"{health}%",

            "Summary":
            "Network operating normally."
        }

        report.generate(
            "reports/executive_report.pdf",
            data
        )