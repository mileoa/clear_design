# В python гоник данных для даты нет. ISO формат учел. А часовой пояс нет.
from datetime import datetime
import pytz


def main():
    date_string = "2024-05-13T14:30:00+00:00"

    try:
        date = datetime.fromisoformat(date_string)
        moscow_tz = pytz.timezone("Europe/Moscow")
        date_moscow = date.astimezone(moscow_tz)
        print(f"Date (Moscow): {date_moscow}")

    except ValueError as e:
        print(f"Ошибка парсинга: {e}")


if __name__ == "__main__":
    main()
