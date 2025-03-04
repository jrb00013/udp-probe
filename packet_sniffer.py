import socket
import struct
import logging

# Set up logging for the packet sniffer
logging.basicConfig(filename="sniffer_log.txt", level=logging.INFO, format='%(asctime)s - %(message)s')

# Create a raw socket to capture packets
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

def sniff_packets():
    print("Sniffing packets...")
    while True:
        raw_packet = sniffer.recvfrom(65565)[0]  # Receive raw packets
        udp_header = raw_packet[20:28]  # UDP header starts after the IP header (20 bytes)
        unpacked_data = struct.unpack('!HHHH', udp_header)
        src_port, dest_port, length, checksum = unpacked_data
        logging.info(f"Captured UDP Packet - Src Port: {src_port}, Dest Port: {dest_port}, Length: {length}")
        print(f"Captured UDP Packet - Src Port: {src_port}, Dest Port: {dest_port}, Length: {length}")

if __name__ == "__main__":
    sniff_packets()
