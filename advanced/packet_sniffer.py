# TODO: Capture network packets (lab environment only)
from scapy.all import sniff

def packet_callback(packet):
    # TODO: Inspect packet and print summary
    pass

if __name__ == "__main__":
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, count=10)  # example: capture 10 packets
