def is_leap(year):
    """Determine whether a year is a leap year

    Args:
        year (int): Year that needs to be checked

    Returns:
        bool: True if the entered year is a leap year, False if it isn't
    """
    leap = False

    if year % 4 == 0:  # year needs to be devisible by 4
        # when the year is divisible by 100, it should also be divisible by 400
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        elif year % 100 != 0:
            leap = True

    return leap
