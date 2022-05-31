import datetime


def replace_format(date):
    date = datetime.datetime.strptime(date, "%d-%m-%Y")


def change_format(date):
    if date.find("января") != -1:
        date.replace(" января, ", "-01-")

    elif date.find("февраля") != -1:
        date.replace(" февраля, ", "-02-")

    elif date.find("марта") != -1:
        date.replace(" марта, ", "-03-")

    elif date.find("апреля") != -1:
        date.replace(" апреля, ", "-04-")

    elif date.find("мая") != -1:
        date.replace(" мая, ", "-05-")

    elif date.find("июня") != -1:
        date.replace(" июня, ", "-06-")

    elif date.find("июля") != -1:
        date.replace(" июля, ", "-07-")

    elif date.find("августа") != -1:
        date.replace(" августа, ", "-08-")

    elif date.find("сентября") != -1:
        date.replace(" сентября, ", "-09-")

    elif date.find("октября") != -1:
        date.replace(" октября, ", "-10-")

    elif date.find("ноября") != -1:
        date.replace(" ноября, ", "-11-")

    elif date.find("декабря") != -1:
        date.replace(" декабря, ", "-12-")
    else:
        print("mistake")
    #
    # if "января" in date:
    #     date.replace(" января, ", "-01-")
    #
    # elif "февраля" in date:
    #     date.replace(" февраля, ", "-02-")
    #     # replace_format(date)
    #
    # elif "марта" in date:
    #     date.replace(" марта, ", "-03-")
    #     # replace_format(date)
    #
    # elif "апреля" in date:
    #     date.replace(" апреля, ", "-04-")
    #     # replace_format(date)
    #
    # elif "мая" in date:
    #     date.replace(" мая, ", "-05-")
    #     # replace_format(date)
    #
    # elif "июня" in date:
    #     date.replace(" июня, ", "-06-")
    #     # replace_format(date)
    #
    # elif "июля" in date:
    #     date.replace(" июля, ", "-07-")
    #     # replace_format(date)
    #
    # elif "августа" in date:
    #     date.replace(" августа, ", "-08-")
    #     # replace_format(date)
    #
    # elif "сентября" in date:
    #     date.replace(" сентября, ", "-09-")
    #     # replace_format(date)
    #
    # elif "октября" in date:
    #     date.replace(" октября, ", "-10-")
    #     # replace_format(date)
    #
    # elif "ноября" in date:
    #     date.replace(" ноября, ", "-11-")
    #     # replace_format(date)
    #
    # elif "декабря" in date:
    #     date.replace(" декабря, ", "-12-")
    #     # replace_format(date)



