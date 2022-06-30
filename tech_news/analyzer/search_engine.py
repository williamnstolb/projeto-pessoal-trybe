from tech_news.database import search_news
from locale import setlocale, LC_ALL
from datetime import datetime


# Requisito 6
def search_by_title(title):
    # Source: https://www.mongodb.com/docs/atlas
    # /schema-suggestions/case-insensitive-regex/
    news_list = list()
    for new in search_news({"title": {"$regex": title, "$options": "i"}}):
        news_list.append((new["title"], new["url"]))
    return news_list


# Requisito 7
def search_by_date(date):
    # Source: https://www.programiz.com/python-programming/datetime/strptime
    news_list = list()
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    try:
        new_format_date = datetime.strptime(
            date, "%Y-%m-%d").strftime("%-d de %B de %Y")
        for new in search_news({"timestamp": new_format_date}):
            news_list.append((new["title"], new["url"]))
        return news_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news_list = list()
    for new in search_news({"tags": {"$regex": tag, "$options": "i"}}):
        news_list.append((new["title"], new["url"]))
    return news_list


# Requisito 9
def search_by_category(category):
    news_list = list()
    for new in search_news(
            {"category": {"$regex": category, "$options": "i"}}):
        news_list.append((new["title"], new["url"]))
    return news_list
