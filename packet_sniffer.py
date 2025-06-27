import socket
import struct
import logging
from colorama import init, Fore

init(autoreset=True)
logging.basicConfig(filename="udp_sniffer.log", level=logging.INFO, format='%(asctime)s - %(message)s')

def sniff_packets(filter_port=None):
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    print(Fore.CYAN + "[*] Sniffing UDP packets...")

    try:
        while True:
            raw_packet = sniffer.recvfrom(65535)[0]
            ip_header = struct.unpack('!BBHHHBBH4s4s', raw_packet[:20])
            udp_header = struct.unpack('!HHHH', raw_packet[20:28])

            src_ip = socket.inet_ntoa(ip_header[8])
            dest_ip = socket.inet_ntoa(ip_header[9])
            src_port, dest_port, length, checksum = udp_header

            if filter_port and src_port != filter_port and dest_port != filter_port:
                continue

            payload = raw_packet[28:].decode(errors='ignore')
            print(Fore.YELLOW + f"UDP {src_ip}:{src_port} -> {dest_ip}:{dest_port} | Length: {length}")
            print(Fore.GREEN + f"Payload: {payload[:100]}")

            logging.info(f"{src_ip}:{src_port} -> {dest_ip}:{dest_port} | Payload: {payload}")

    except KeyboardInterrupt:
        print(Fore.RED + "\n[*] Sniffer stopped.")

if __name__ == "__main__":
    sniff_packets(filter_port=None)
