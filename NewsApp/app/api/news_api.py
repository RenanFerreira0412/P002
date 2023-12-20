import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()


class NewsApi:
    def __init__(self):
        self.api_key = getenv('API_KEY')
        self.articles = []
        self.get_top_headlines_news()

    def get_news(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            news = response.json()
            print('os babados  ', news)
            self.articles = news['articles']
        except requests.exceptions.RequestException as e:
            return {"error": f"Erro ao obter dados da API: {e}"}

    def get_top_headlines_news(self):
        url = f"https://newsapi.org/v2/top-headlines?country=br&apiKey={self.api_key}"

        print(url)
        self.get_news(url=url)

    def get_specific_news(self, topic, fromDate, toDate, language):
        url = f"https://newsapi.org/v2/everything?q={topic}&from={fromDate}&to={toDate}&sortBy=popularity&language={language}&apiKey={self.api_key}"

        self.get_news(url=url)
