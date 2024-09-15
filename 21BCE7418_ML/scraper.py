import requests
from models import Document
from bs4 import BeautifulSoup
import threading

def scrape_news():
    url = "https://newswebsite.com/latest"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = soup.find_all("article")
    for article in articles:
        content = article.get_text()
        embedding = model.encode(content)
        new_doc = Document(content=content, embedding=embedding)
        db.session.add(new_doc)
    
    db.session.commit()

def run_scraper():
    while True:
        scrape_news()
        time.sleep(3600)  # Run every hour

scraper_thread = threading.Thread(target=run_scraper)
scraper_thread.start()
