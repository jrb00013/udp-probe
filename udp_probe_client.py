import socket
import time
import argparse

def udp_probe_client(target_ip, target_port, interval=1.0, count=10, echo=True):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2.0)

    print(f"[+] Sending {count} UDP packets to {target_ip}:{target_port} every {interval}s")

    for i in range(1, count + 1):
        payload = f"probe_id={i}, timestamp={time.time()}"
        start = time.time()
        sock.sendto(payload.encode(), (target_ip, target_port))

        try:
            if echo:
                data, _ = sock.recvfrom(2048)
                rtt = (time.time() - start) * 1000
                print(f"[{i}] Echo received | RTT: {rtt:.2f} ms | {data.decode()}")
            else:
                print(f"[{i}] Sent payload: {payload}")

        except socket.timeout:
            print(f"[{i}] No response (timeout)")

        time.sleep(interval)

    sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UDP Probe Sender")
    parser.add_argument("--ip", default="127.0.0.1", help="Target IP")
    parser.add_argument("--port", type=int, default=9999, help="Target Port")
    parser.add_argument("--interval", type=float, default=1.0, help="Interval between packets")
    parser.add_argument("--count", type=int, default=10, help="Number of packets to send")
    parser.add_argument("--no-echo", action="store_true", help="Disable echo expectation")
    args = parser.parse_args()

    udp_probe_client(args.ip, args.port, args.interval, args.count, not args.no_echo)
