import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression pattern to match the 12-hour time format
    # Adjusted to expect space between time and AM/PM
    pattern = r"(\d{1,2})(:\d{2})?\s?(AM|PM)\s?to\s?(\d{1,2})(:\d{2})?\s?(AM|PM)"

    # Match the pattern against the input string
    match = re.match(pattern, s)

    if match:
        # Extract the matched groups from the pattern
        hour1, minute1, meridiem1, hour2, minute2, meridiem2 = match.groups()

        # Convert the hours to integers
        hour1 = int(hour1)
        hour2 = int(hour2)

        # Check if the hours are valid
        if (hour1 < 1 or hour1 > 12) or (hour2 < 1 or hour2 > 12):
            raise ValueError("Invalid hour")

        # Check if the minutes are valid
        if minute1 and int(minute1[1:]) > 59 or minute2 and int(minute2[1:]) > 59:
            raise ValueError("Invalid minute")

        # If minutes are not given, assume they are '00'
        if not minute1:
            minute1 = ':00'
        if not minute2:
            minute2 = ':00'

        # Convert the 12-hour format to 24-hour format
        if meridiem1 == "PM" and hour1 != 12:
            hour1 += 12
        elif meridiem1 == "AM" and hour1 == 12:
            hour1 = 0

        if meridiem2 == "PM" and hour2 != 12:
            hour2 += 12
        elif meridiem2 == "AM" and hour2 == 12:
            hour2 = 0

        # Format the hours and minutes with leading zeroes
        time1 = f"{hour1:02}{minute1 if minute1 else ''}"
        time2 = f"{hour2:02}{minute2 if minute2 else ''}"

        # Return the converted time range
        return f"{time1} to {time2}"

    else:
        raise ValueError("Invalid time format")

if __name__ == "__main__":
    main()
