import time
import datetime
import dateutil
import calendar


def last_day(date1):
    month_info = calendar.monthrange(date1.year, date1.month)
    print(datetime.date(date1.year, date1.month, month_info[1]))


def workdays(date1, date2):
    working_days = 0
    delta = date2 - date1
    if delta.days < 0:
        raise Exception
    for days in range(delta.days):
        calcdate = date1 + datetime.timedelta(days=days)
        if calcdate.weekday() < 5:
            working_days += 1
    print(working_days)


last_day(datetime.date.today())
workdays(datetime.date.today(), datetime.date(2020, 11, 1))
