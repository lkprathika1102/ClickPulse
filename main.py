import csv
import time
import threading
from datetime import datetime
from pynput import mouse

count = 0
lock = threading.Lock()

def on_click(x, y, button, pressed):
    global count
    if pressed:
        with lock:
            count += 1

def log_data():
    global count
    while True:
        time.sleep(60)
        with lock:
            current_count = count
            count = 0
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open("click_log.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, current_count])
        
        print(f"[{timestamp}] Recorded {current_count} clicks.")

def main():
    with open("click_log.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "count"])

    listener = mouse.Listener(on_click=on_click)
    listener.start()

    logger_thread = threading.Thread(target=log_data, daemon=True)
    logger_thread.start()

    print("ClickPulse is running. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping ClickPulse...")
        listener.stop()

if __name__ == "__main__":
    main()