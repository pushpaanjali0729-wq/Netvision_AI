# reports/pdf_report.py

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


class PDFReport:

    def generate(
            self,
            filename,
            report_data
    ):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph(
                "NetVision AI Security Report",
                styles["Title"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        for key, value in report_data.items():

            elements.append(
                Paragraph(
                    f"<b>{key}</b>: {value}",
                    styles["Normal"]
                )
            )

        doc.build(elements)

        print(
            f"Report saved: {filename}"
        )