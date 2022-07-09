import requests
from models import CertainNews
from bs4 import BeautifulSoup


# Информация по каждой статье
main_articles_list = []
# Список ссылок на новости для данной страницы
main_refs_list = []
# Список заголовков для данной страницы
main_titles_list = []


def url_response(url: str):
    response = requests.get(url)
    return print("Response status: ", response.status_code)


def certain_page_parsing(url: str):

    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    news_refs = soup.find_all(class_='item', href=True)
    news_datetime = soup.find_all('time')
    news_titles = soup.find_all('span', class_='title')
    news_types = soup.find_all('span', class_='parent')

    main_refs_list_creating(news_refs)
    main_titles_list_creating(news_titles)
    main_articles_list_creating(news_datetime, news_titles, news_types)


def sections_parsing(url: str):

    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    _list = soup.select("nav > a")

    sections_list_refs = []
    sections_list_titles = []

    for i in range(len(_list)):
        sections_list_refs.append(url[:-1] + _list[i].get("href"))
        sections_list_titles.append(_list[i].text)

    global main_refs_list
    main_refs_list = sections_list_refs

    global main_titles_list
    main_titles_list = sections_list_titles

    return sections_list_refs, sections_list_titles


def main_refs_list_creating(refs: list):
    for link in refs:
        main_refs_list.append('https://inc-news.ru' + link.get('href'))


def main_titles_list_creating(titles: list):
    for i in range(len(titles)):
        main_titles_list.append(titles[i].text)


def main_articles_list_creating(datetime, titles, types: list):
    for i in range(len(titles)):
        main_articles_list.append(CertainNews(ref=main_refs_list[i], datetime=datetime[i].text, title=titles[i].text, type=types[i].text))


def get_articles_list():
    return main_articles_list


def get_refs_list():
    return main_refs_list


def get_titles_list():
    return main_titles_list


def clear():
    main_articles_list.clear()
    main_refs_list.clear()
