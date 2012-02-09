from datetime import datetime

# Adapted from http://stackoverflow.com/questions/1551382/python-user-friendly-time-format
def pretty_date(time=False):
    """
    Expects a datetime in utc.
    """
    now = datetime.utcnow()
    diff = now - time
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return  "a minute ago"
        if second_diff < 3600:
            return str( second_diff / 60 ) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str( second_diff / 3600 ) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        diff = day_diff/7
        diff_string = "week"
        if diff > 1:
            diff_string = "weeks"
        return  "%s %s ago" % (str(diff), diff_string)
    if day_diff < 365:
        diff = day_diff/30
        diff_string = "month"
        if diff > 1:
            diff_string = "months"
        return "%s %s ago" % (str(diff), diff_string)
    
    diff_string = "year"
    diff = day_diff/365
    if diff > 1:
        diff_string = "years"
    return "%s %s ago" % (str(diff), diff_string)
