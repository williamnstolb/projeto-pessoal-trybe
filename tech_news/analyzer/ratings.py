from tech_news.database import db


# Requisito 10
def top_5_news():
    news_list = list()
    for new in db.news.find().sort(
            [("comments_count", -1), ("title", -1)]).limit(5):
        news_list.append((new["title"], new["url"]))
    return news_list


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
