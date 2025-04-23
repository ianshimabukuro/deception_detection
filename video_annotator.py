import keyboard
import time

# CONFIG
fps = 30
interval = 1 / fps
duration = 10  # in seconds, or use another stopping mechanism

label_list = []
print("🎥 Starting label capture... Press 'a' for FALSE, 'd' for TRUE, else NEUTRAL.")
print("⏳ Recording... Press 'esc' to stop early.")

start_time = time.time()

try:
    while True:
        if keyboard.is_pressed('esc'):
            print("🛑 Stopped early.")
            break

        if keyboard.is_pressed('a'):
            label_list.append("false")
        elif keyboard.is_pressed('d'):
            label_list.append("truth")
        else:
            label_list.append("neutral")

        time.sleep(interval)

        # Optional: Stop automatically after a set duration
        if time.time() - start_time > duration:
            print("⏰ Reached duration limit.")
            break

except KeyboardInterrupt:
    print("Interrupted manually.")

print(f"✅ Labeling complete: {len(label_list)} labels recorded.")