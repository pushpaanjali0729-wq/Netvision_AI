# reports/weekly_report.py

from reports.pdf_report import PDFReport


class WeeklyReport:

    def generate(
        self,
        weekly_packets,
        weekly_threats
    ):

        report = PDFReport()

        data = {

            "Weekly Packets":
                weekly_packets,

            "Weekly Threats":
                weekly_threats
        }

        report.generate(
            "reports/weekly_report.pdf",
            data
        )