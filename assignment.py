def leap_year(year: int) -> int:
    '''
    leap_year() -> number of days in February based on leap year

    Returns 29 if the year is a leap year, otherwise returns 28.
    This function checks the leap year logic (divisible by 4, divisible by 400).
    '''
    if year % 400 == 0:
        return 29
    elif year % 100 == 0:
        return 28
    elif year % 4 == 0:
        return 29
    else:
        return 28


def mon_max(year: int) -> dict:
    '''
    mon_max() -> dictionary of maximum days in each month of the year

    Returns a dictionary where the key is the month number (1-12) and the value is the number of days in that month.
    Adjusts February based on whether the year is a leap year or not.
    '''
    feb_max = leap_year(year)  # Use leap_year() function to get February days based on the year
    return {
        1: 31, 2: feb_max, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }


def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Returns the date for the next day of the given date in YYYY-MM-DD format.
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    mon_max_days = mon_max(year)  # Pass the year to mon_max()

    tmp_day = day + 1  # next day

    if tmp_day > mon_max_days[month]:
        tmp_day = 1  # if tmp_day > this month's max, reset to 1
        tmp_month = month + 1
    else:
        tmp_month = month

    if tmp_month > 12:
        tmp_month = 1
        year += 1

    next_date = f"{year}-{tmp_month:02}-{tmp_day:02}"

    return next_date


# Testing the refactored functions
if __name__ == "__main__":
    print(after('2023-01-25'))  # Test after function
    print(after('2016-02-28'))  # Test leap year scenario
    print(after('2025-12-31'))  # Test year-end date
