import requests
from bs4 import BeautifulSoup
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from data_format import change_format

base_url = "https://проконференции.рф/events/"

connection = psycopg2.connect(user="postgres",
                              password="912368.Noris",
                              host="127.0.0.1",
                              port="5432",
                              database="telegram_bot")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("Вы подключены к - ", record, "\n")


def parse_data():
    global name, event_arranger, event_data, subjects
    main_pages = requests.get(base_url)
    soup = BeautifulSoup(main_pages.text, "html.parser")

    events_names = soup.find_all("h2", "tb-heading")
    # events_date = soup.find_all("div",
    #                             attrs={"data-toolset-blocks-fields-and-text": "35e04a435ec2b02ee551e339b426cf53"})
    events_subject = soup.find_all("div", attrs={"data-toolset-blocks-field": "eb9f280390a737e30ae29856e0db88b8"})
    next_url = soup.find_all("a", "wp-block-toolset-blocks-container tb-container")

    for name in events_names:
        print(name.text)
        sqlcom = "INSERT INTO events (event_name) VALUES (%s);"
        args = [name.text]
        cursor.execute(sqlcom, args)
    print("_______________")
    # for date in events_date:
    #     print(date.text[20:])
    # print(change_format(date.text[20:]))
    # d = "INSERT INTO events (date) VALUES ('" + str(date.text[20:]) + "');"
    # cursor.execute(d)
    print("_______________")
    for subjects in events_subject:
        print(subjects.getText)
        sqlcom = "INSERT INTO events (subject) VALUES (%s);"
        args = [subjects.text]
        cursor.execute(sqlcom, args)
    print("_______________")
    for url in next_url:
        urls = [url.get('href')]
        while len(urls) > 0:
            url = urls.pop(0)
            response = requests.get(url)
            soup_pages = BeautifulSoup(response.text, "html.parser")
            event_data = soup_pages.find('div',
                                         attrs={"data-toolset-blocks-button": "e35d61f6e75f753121cc884e5fdefdec"}).find(
                "a", attrs={"target": "_blank"}).get('href')
            event_arranger = soup_pages.find('div', attrs={
                "data-toolset-blocks-button": "07481b789a0959f00ba23ce903b28d1a"}).find("a",
                                                                                        attrs={"target": "_blank"}).get(
                'href')
            print(event_data)
            print(event_arranger)
            print("==========")
            sqlcom = "INSERT INTO events (arranger, event_link) VALUES (%s, %s);"
            args = [event_arranger, event_data]
            cursor.execute(sqlcom, args)
    connection.commit()
    # sqlcom = "INSERT INTO events (event_name, arranger, subject, event_link) VALUES (%s, %s, %s, %s);"
    # args = [name.text, event_arranger, subjects, event_data]
    # cursor.execute(sqlcom, args)
    # connection.commit()
    return


parse_data()
