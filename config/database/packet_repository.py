# database/packet_repository.py

from database.db import db


class PacketRepository:

    @staticmethod
    def save_packet(
            timestamp,
            src_ip,
            dst_ip,
            protocol,
            packet_length
    ):

        db.cursor.execute(
            """
            INSERT INTO packets(
                timestamp,
                src_ip,
                dst_ip,
                protocol,
                packet_length
            )
            VALUES(?,?,?,?,?)
            """,
            (
                timestamp,
                src_ip,
                dst_ip,
                protocol,
                packet_length
            )
        )

        db.commit()