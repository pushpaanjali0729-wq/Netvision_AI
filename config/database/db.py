# database/db.py

import sqlite3
from config.settings import DATABASE_PATH


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(
            DATABASE_PATH,
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS packets(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            src_ip TEXT,

            dst_ip TEXT,

            protocol TEXT,

            packet_length INTEGER

        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS anomalies(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            src_ip TEXT,

            dst_ip TEXT,

            threat_type TEXT,

            threat_score REAL

        )
        """)

        self.connection.commit()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()


db = Database()