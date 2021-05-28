import requests
from bs4 import BeautifulSoup

from telegram_bot import TelegramBot
from yml_config import YMLConfig

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}


class StockNotifier:

    def check(self):
        try:
            self.config = YMLConfig().config
            self.telegram_bot = TelegramBot(self.config)
            [self.check_inventories(page, url) for page in self.config['pages'] for url in page['urls']]
        except Exception as e:
            print(e)

    def check_inventories(self, page, url):
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            self.telegram_bot.page_error(url, page.status_code)
        else:
            if self.is_in_stock(response.content, page):
                self.telegram_bot.in_stock(url)
            else:
                print('Out of Stock: {}'.format(url))

    def is_in_stock(self, html, page) -> bool:
        soup = BeautifulSoup(html, 'html.parser')
        button_disabled = soup.find(page['element'], page['identifier'])
        return button_disabled is None
