import calendar
from datetime import datetime

if __name__ == "__main__":
    dt_str = input().strip()
    dt = datetime.strptime(dt_str, "%m %d %Y")
    day = calendar.day_name[dt.weekday()]
    print(day.upper())
