import socket
import json
import time
import logging

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Set up logging
logging.basicConfig(filename=config['log_file'], level=logging.INFO, format='%(asctime)s - %(message)s')

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((config['host'], config['port']))

def probe():
    print(f"Listening on {config['host']}:{config['port']}...")
    while True:
        data, addr = sock.recvfrom(1024)  # Receive UDP packets
        logging.info(f"Received message from {addr}: {data.decode()}")
        print(f"Received message from {addr}: {data.decode()}")

        # Optionally, handle data or trigger other actions
        if data.decode() == 'exit':
            print("Exiting probe...")
            break

if __name__ == "__main__":
    probe()
