# core/packet_capture.py

from scapy.all import sniff
from datetime import datetime

from core.packet_parser import PacketParser
from database.packet_repository import PacketRepository

from config.logging_config import logger


class PacketCapture:

    def process_packet(self, packet):

        parsed = PacketParser.parse(packet)

        if not parsed:
            return

        PacketRepository.save_packet(

            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            parsed["src_ip"],
            parsed["dst_ip"],
            parsed["protocol"],
            parsed["packet_length"]
        )

        logger.info(
            f'{parsed["src_ip"]} -> '
            f'{parsed["dst_ip"]}'
        )

    def start(self):

        logger.info("Packet Capture Started")

        sniff(

            prn=self.process_packet,

            store=False
        )