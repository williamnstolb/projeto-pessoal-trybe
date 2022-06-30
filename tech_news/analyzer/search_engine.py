from tech_news.database import search_news


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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
