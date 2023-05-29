import time
import os

def focus_clock(duration):
    start_time = time.time()
    end_time = start_time + duration * 60  # Convert duration from minutes to seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60

        # Clear the console screen (works on Windows, macOS, and Linux)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"Focus Clock - {minutes:02d}:{seconds:02d}")
        time.sleep(1)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Focus Clock - 00:00")
    print("Time's up! Your focus session has ended.")
