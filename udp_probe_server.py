import socket
import json
import time
import logging
import csv

with open("config.json", "r") as f:
    config = json.load(f)

logging.basicConfig(filename=config['log_file'], level=logging.INFO, format='%(asctime)s - %(message)s')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((config['host'], config['port']))

seen_ids = set()
packet_count = 0
start_time = time.time()

print(f"[+] UDP Listener active on {config['host']}:{config['port']}")

def extract_probe_info(data):
    try:
        items = dict(item.split('=') for item in data.strip().split(', '))
        return int(items.get("probe_id", -1)), float(items.get("timestamp", 0.0))
    except:
        return -1, 0.0

def probe():
    global packet_count
    with open("udp_session.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "From", "RTT_ms", "Message"])

        while True:
            try:
                data, addr = sock.recvfrom(2048)
                recv_time = time.time()
                msg = data.decode(errors='ignore')

                probe_id, sent_ts = extract_probe_info(msg)
                rtt = (recv_time - sent_ts) * 1000 if sent_ts > 0 else -1

                duplicate = probe_id in seen_ids
                if not duplicate:
                    seen_ids.add(probe_id)

                packet_count += 1

                logging.info(f"{addr} | ID: {probe_id} | RTT: {rtt:.2f} ms")
                print(f"[{packet_count}] {addr} | ID: {probe_id} | RTT: {rtt:.2f} ms")

                writer.writerow([probe_id, addr[0], f"{rtt:.2f}", msg])

                if config.get("echo", False):
                    sock.sendto(f"ACK: {probe_id}".encode(), addr)

            except KeyboardInterrupt:
                break

    duration = time.time() - start_time
    print(f"[-] Session ended. {packet_count} packets in {duration:.2f} seconds.")

if __name__ == "__main__":
    probe()
