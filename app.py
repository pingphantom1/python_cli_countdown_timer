import time
import sys
import tty
import termios
import select


def get_duration_before_countdown():
    while True:
        raw_countdown_duration = input("Enter the duration before countdown begins in the format HHMMSS (e.g. 013045): ")

        if not raw_countdown_duration.isdigit() or len(raw_countdown_duration) != 6:
            print("Invalid input. please enter exactly 6 digits in the format HHMMSS (e.g. 010430)")
            continue

        try:
            hh = int(raw_countdown_duration[:2])
            mm = int(raw_countdown_duration[2:4])
            ss = int(raw_countdown_duration[4:6])

            if hh > 23:
                print("The hour (HH) cannot be greater than 23")
            if mm > 60 or ss > 60:
                print("The minute (mm) or the seconds (ss) can't be greater than 60")

        except ValueError:
            print('invalid input')

        break

    return hh, mm, ss

hour, minute, second = get_duration_before_countdown()

# print(hour)
# print(minute)
# print(second)

# current_formatted_time = time.strftime('%H:%M:%S', time.localtime())
# print(current_formatted_time)

def countdown_time(hour=0, minute=0, second=0):
    paused = False
    total_seconds = hour * 3600 + minute * 60 + second
    old_settings = termios.tcgetattr(sys.stdin)


    print(f"Countdown for {hour}h {minute}m {second}s...")
    print("Press P to pause/resume")

    try:
        # Read individual keypresses without pressing Enter
        tty.setcbreak(sys.stdin.fileno())

        end_time = time.monotonic() + total_seconds
        while total_seconds > 0:
            # Check for keyboard input without bblocking
            if select.select([sys.stdin], [], [], 0)[0]:
                key = sys.stdin.read(1).lower()

                if key == 'p':
                    # change value of the paused variable when p is pressed
                    paused = not paused

                    if paused:
                        print("\nPaused. Press P to resume.")
                    else:
                        print("Resumed.")

                        # Restart countdown from remaining time
                        end_time = time.monotonic() + total_seconds


            if not paused:
                total_seconds = max(
                    0, int(end_time - time.monotonic() + 0.999999)
                )
                mins, secs = divmod(total_seconds, 60)
                hours, mins = divmod(mins, 60)
                
                sys.stdout.write(f"\rTime left: {hours:02d}:{mins:02d}:{secs:02d}")
                sys.stdout.flush()
                time.sleep(0.5)
            else:
                time.sleep(0.5)

        print("\nYour timer has finished!")

    finally:
        # Restore the terminal to it's original state
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

countdown_time(hour, minute, second)
