import time
from datetime import datetime


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

print(hour)
print(minute)
print(second)

# def countdown_time(hour, minute, second):
#     current_formatted_time = time.strftime('%H:%M:%S', time.localtime())

#     print("countdown ends in: ")
