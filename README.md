# ClickPulse

# ClickPulse
ClickPulse is a mouse activity monitor. It tracks the volume of clicks over time to analyze usage patterns without recording where you click or what you are clicking on, ensuring absolute user privacy. It is super simple to understand and use. Now go on, try it out and spy on your click time with ClickPulse.

## System Architecture
The system consists of two primary modules:

Tracking (main.py):
- A background process that hooks into system-level mouse events using pynput.
- Uses a thread-safe threading.Lock to ensure counts are accurate across OS event threads.
- Flushes data to click_log.csv every 60 seconds and resets the atomic counter.

Visualization Engine (plot_activity.py):
- An analysis script that processes the CSV using Pandas.
- Generates a high-resolution Timeline Plot (Clicks per minute over time).
- Generates an Hourly Heatmap to visualize peak activity periods throughout the day.

## Setup & Installation
Prerequisites
- Python 3.12 (Recommended for stability and pre-compiled binary support).
- macOS Permissions: macOS requires explicit permission to monitor mouse events.

Installation Steps (macOS)
Clone the repository:
```bash
git clone <repository-url>
cd click-pulse
```

Install Python 3.12 (via Homebrew):
```bash
brew install python@3.12
```

Initialize a Virtual Environment:
```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Install Dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage
1. Start Tracking
Run the daemon to begin capturing activity:
```bash
python main.py
```
The daemon will log activity to the console every minute. Press Ctrl+C to stop.

2. Generate Visuals
Once you have collected data, run the visualization script:
```bash
python plot_activity.py
```
This will produce two files in the project root:
- click_timeline.png: A linear graph of your clicking volume.
- click_heatmap.png: A grid showing your most active hours.


<img width="963" height="476" alt="Screen Shot 2026-08-02 at 15 24 27 PM" src="https://github.com/user-attachments/assets/bb6f44e2-9720-4695-9e3e-0befff054f05" />


<img width="3600" height="1800" alt="click_timeline" src="https://github.com/user-attachments/assets/fffb3f6c-79fc-43a2-97d5-adc3fa3c652f" />


## Troubleshooting macOS Permissions 
If the tracker runs but records 0 clicks:
1. Open System Settings 
2. Go to Privacy & Security 
3. Go to Accessibility
4. Find your Terminal (or VS Code) in the list.
5. Toggle the switch to ON.
6. Restart the terminal and run python main.py again.

For Windows, it just works directly.

## Testing Guide
- Daemon Test: Run main.py and click around for 2 minutes. Verify that the console prints Recorded X clicks every 60 seconds.
- Visualization Test: Run plot_activity.py and verify that the two PNG files are generated with correct data.
