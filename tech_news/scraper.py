import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    headers = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, timeout=3, headers=headers)
        response.raise_for_status()
    except (requests.HTTPError, requests.Timeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    location = ".entry-title a::attr(href)"
    return selector.css(location).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    location = ".next.page-numbers::attr(href)"
    return selector.css(location).get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news = dict()
    news = {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".entry-title::text").get(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": len(selector.css(".comment-content p").getall()),
        "summary": selector.xpath("string(//p)").get(),
        "tags": selector.css(".post-tags ul li a::text").getall(),
        "category": selector.css(".category-style .label::text").get(),
    }
    return news


# Requisito 5
def get_tech_news(amount):
    BASE_LINK = "https://blog.betrybe.com"
    trybe_all_news = list()
    next_page_link = BASE_LINK
    while len(trybe_all_news) < amount:
        html_content = fetch(next_page_link)
        links = scrape_novidades(html_content)
        for link in links:
            news = scrape_noticia(fetch(link))
            trybe_all_news.append(news)
        next_page_link = scrape_next_page_link(html_content)
    create_news(trybe_all_news[:amount])
    return trybe_all_news[:amount]
