def readable_timedelta(days):
    # insert your docstring here
    """Returns a string of the number of weeeks and days included in days"""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
