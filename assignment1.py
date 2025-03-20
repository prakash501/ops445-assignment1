def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap years.
    This function has been tested to work for years after 1582.
    '''
    
    # Split the given date string into year, month, and day as integers
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    # Determine if it's a leap year (initial check)
    lyear = year % 4
    if lyear == 0:
        feb_max = 29  # Leap year, February has 29 days
    else:
        feb_max = 28  # Non-leap year, February has 28 days

    # Refine leap year check for century years (e.g., 1900, 2000)
    lyear = year % 100
    if lyear == 0:
        feb_max = 28  # Century years are NOT leap years unless divisible by 400

    # Final leap year check for years divisible by 400 (e.g., 1600, 2000)
    lyear = year % 400
    if lyear == 0:
        feb_max = 29  # Divisible by 400 means it's a leap year

    # Dictionary defining max days in each month (handles leap years)
    mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 
                7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }

    # Calculate the next day
    tmp_day = day + 1  

    if tmp_day > mon_max[month]:  # If next day exceeds max days in the month
        to_day = 1  # Reset day to 1
        tmp_month = month + 1  # Move to next month
    else:
        to_day = tmp_day
        tmp_month = month  # Stay in the same month

    if tmp_month > 12:  # If month exceeds December, reset to January and increment year
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month

    # Format and return the next date as YYYY-MM-DD
    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date

# Testing the function
if __name__ == "__main__":
    print(after('2023-01-25'))  # Expected output: 2023-01-26
    print(after('2016-02-28'))  # Expected output: 2016-02-29 (leap year)
    print(after('2025-12-31'))  # Expected output: 2026-01-01
