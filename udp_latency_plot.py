import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "udp_session.csv"
OUTPUT_IMAGE = "rtt_latency_plot.png"

def main():
    try:
        df = pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        print(f"CSV file '{CSV_FILE}' not found.")
        return

    if "rtt_ms" not in df.columns:
        print("CSV does not contain 'rtt_ms' column.")
        print("Available columns:", df.columns.tolist())
        return

    plt.figure()
    plt.plot(df.index, df["rtt_ms"])
    plt.xlabel("Packet Index")
    plt.ylabel("RTT (ms)")
    plt.title("UDP Packet RTT Latency")
    plt.grid(True)
    plt.savefig(OUTPUT_IMAGE)

    print(f"Latency graph saved as {OUTPUT_IMAGE}")

if __name__ == "__main__":
    main()
