# UDP Probe 

A lightweight toolkit featuring a few automation scripts that mimic Wireshark functionality to capture, analyze, and test UDP traffic.

- Allows a user to test latency, simulate probes, detect packet loss, and visualize data. This tool captures and analyzes UDP traffic similarily to Wireshark.


## How to Use:
1. Set desired filters in `config.json`. Change host and port / log file output to values needed.
2. Run `python udp_probe_server.py` in one terminal or machine to start the server.
3. Run `python udp_probe_client.py --ip 127.0.0.1 --port 9999 --count 20 --interval 0.5` in 2nd terminal or machine to send the test packets
4. Run `sudo python udp_packet_sniffer.py` in a 3rd terminal or machine to sniff the traffic
5. Run `python udp_csv_analyzer.py` after to analyze the results.
6. You will get a report of Packet Count, Packet Loss, Duplicates, and Average RTT

## Requirements:
- Python 3.x
