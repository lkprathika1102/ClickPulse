import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data():
    if not os.path.exists("click_log.csv"):
        print("Error: click_log.csv not found.")
        return None
    
    df = pd.read_csv("click_log.csv")
    if df.empty:
        print("Error: No data available in log file.")
        return None
        
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

def plot_timeline(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df["timestamp"], df["count"], color="#8e44ad", linewidth=2)
    plt.title("Clicks Per Minute Over Time")
    plt.xlabel("Time")
    plt.ylabel("Clicks")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("click_timeline.png", dpi=300)
    plt.close()

def plot_heatmap(df):
    df["hour"] = df["timestamp"].dt.hour
    df["date"] = df["timestamp"].dt.date
    
    pivot = df.pivot_table(index="date", columns="hour", values="count", aggfunc="sum").fillna(0)
    
    plt.figure(figsize=(15, 8))
    plt.imshow(pivot, cmap="Purples", aspect="auto")
    plt.colorbar(label="Total Clicks")
    plt.title("Hourly Click Activity Heatmap")
    plt.xlabel("Hour of Day")
    plt.ylabel("Date")
    plt.xticks(range(24), range(24))
    plt.tight_layout()
    plt.savefig("click_heatmap.png", dpi=300)
    plt.close()

def main():
    df = load_data()
    if df is not None:
        plot_timeline(df)
        plot_heatmap(df)
        print("Visualizations generated: click_timeline.png, click_heatmap.png")

if __name__ == "__main__":
    main()