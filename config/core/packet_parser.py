# core/packet_parser.py

from scapy.all import IP


class PacketParser:

    @staticmethod
    def parse(packet):

        if not packet.haslayer(IP):
            return None

        return {

            "src_ip": packet[IP].src,

            "dst_ip": packet[IP].dst,

            "protocol": packet[IP].proto,

            "packet_length": len(packet)

        }