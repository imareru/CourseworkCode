import requests
from bs4 import BeautifulSoup
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = psycopg2.connect(user="postgres",
                              password="912368.Noris",
                              host="127.0.0.1",
                              port="5432",
                              database="telegram_bot")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# Курсор для выполнения операций с базой данных
cursor = connection.cursor()
cursor.execute("SELECT version();")
# Получить результат
record = cursor.fetchone()
print("Вы подключены к - ", record, "\n")

URL_TEMPLATE = "https://проконференции.рф/events/"


def parse(url):
    
    result_list = {'name': [], 'date': [], 'arranger_contacts': [], 'subject': []}
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    events_names = soup.find_all("h2", "tb-heading")
    for name in events_names:
        name.text
    return name
