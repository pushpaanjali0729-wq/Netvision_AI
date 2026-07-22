# database/anomaly_repository.py

from database.db import db


class AnomalyRepository:

    @staticmethod
    def save_anomaly(
            timestamp,
            src_ip,
            dst_ip,
            threat_type,
            threat_score
    ):

        db.cursor.execute(
            """
            INSERT INTO anomalies(
                timestamp,
                src_ip,
                dst_ip,
                threat_type,
                threat_score
            )
            VALUES(?,?,?,?,?)
            """,
            (
                timestamp,
                src_ip,
                dst_ip,
                threat_type,
                threat_score
            )
        )

        db.commit()