import csv
from statistics import mean, stdev

def analyze_csv(file_path="udp_session.csv"):
    probe_ids = []
    rtts = []
    duplicates = 0

    seen = set()

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pid = int(row["ID"])
            rtt = float(row["RTT_ms"])

            if pid in seen:
                duplicates += 1
            else:
                seen.add(pid)
                probe_ids.append(pid)
                if rtt >= 0:
                    rtts.append(rtt)

    expected = max(probe_ids) if probe_ids else 0
    lost = expected - len(seen)

    print(f"\n📊 UDP Session Report")
    print(f"Total Packets Received: {len(seen)}")
    print(f"Expected Packets:       {expected}")
    print(f"Duplicates:             {duplicates}")
    print(f"Lost Packets:           {lost}")
    if rtts:
        print(f"Average RTT:            {mean(rtts):.2f} ms")
        print(f"RTT Std Dev:            {stdev(rtts):.2f} ms")

if __name__ == "__main__":
    analyze_csv()
