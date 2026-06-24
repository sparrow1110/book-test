from datetime import datetime


MONTHS = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря",
}


def format_text_date():
    now = datetime.now()

    day = now.day
    month = MONTHS[now.month]
    year = now.year

    return f"{day} {month} {year} года"