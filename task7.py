# 1. В этом коде нет инфомрации о часовом поясе. Не понятно в каком часовом поясе записана дата.
# 2. Возможно, cтоит писать формат даты в ISO формате. Иначе по коду в разных местах будет записана дата в разных форматах.
from datetime import datetime
from zoneinfo import ZoneInfo


# было
def main_before():
    date_string = "2024-05-13 14:30:00"
    format = "%Y-%m-%d %H:%M:%S"
    try:
        date = datetime.strptime(date_string, format)
        print("Date:", date)
    except ValueError as e:
        print(e)


def main_after():
    date_string = "2024-05-13T14:30:00+00:00"
    try:
        date = datetime.fromisoformat(date_string)
        print("Date:", date)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main_before()
    main_after()
