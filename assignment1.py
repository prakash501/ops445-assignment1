#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Winter 2025
Program: assignment1.py 
Author: "Prakash Gautam (Pgautam10)"
The python code in this file (assignment1.py) is original work written by
"Aashis Kharel". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    """
    Returns the day of the week for a given date using Sakamoto's algorithm.
    """
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}

    if month < 3:
        year -= 1  # Adjust year for January and February

    num = (year + year // 4 - year // 100 + year // 400 + offset[month] + date) % 7
    return days[num]

def leap_year(year: int) -> bool:
    """
    Determines if a year is a leap year.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """
    Returns the maximum number of days in a given month and year.
    """
    if month == 2:
        return 29 if leap_year(year) else 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 0  # Invalid month

def after(date: str) -> str:
    """
    Returns the next day's date in YYYY-MM-DD format.
    Handles leap years and transitions between months and years.
    """
    year, month, day = map(int, date.split('-'))
    day += 1

    if day > mon_max(month, year):
        day = 1
        month += 1

    if month > 12:
        month = 1
        year += 1

    return f"{year}-{month:02}-{day:02}"

def valid_date(date: str) -> bool:
    """
    Validates a date string in the format YYYY-MM-DD.
    """
    try:
        parts = date.split('-')
        if len(parts) != 3:
            return False
        if not (parts[0].isdigit() and len(parts[0]) == 4):
            return False

        year, month, day = map(int, parts)
        if month < 1 or month > 12:
            return False
        if day < 1 or day > mon_max(month, year):
            return False
        return True
    except:
        return False

def day_count(start_date: str, stop_date: str) -> int:
    """
    Counts the number of weekend days (Saturday and Sunday) between two dates inclusive.
    """
    if start_date > stop_date:
        start_date, stop_date = stop_date, start_date

    count = 0
    current_date = start_date

    while current_date <= stop_date:
        y, m, d = map(int, current_date.split('-'))
        if day_of_week(y, m, d) in ['sat', 'sun']:
            count += 1
        current_date = after(current_date)

    return count

def usage():
    """
    Prints usage instructions and exits the program.
    """
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit()

def main():
    if len(sys.argv) != 3:
        usage()

    d1, d2 = sys.argv[1], sys.argv[2]

    if not valid_date(d1) or not valid_date(d2):
        usage()

    start, end = sorted([d1, d2])
    weekends = day_count(start, end)
    print(f"The period between {start} and {end} includes {weekends} weekend days.")

if __name__ == "__main__":
    main()
