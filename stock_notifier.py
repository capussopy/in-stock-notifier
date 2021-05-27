import requests
from bs4 import BeautifulSoup

from telegram_bot import TelegramBot
from ymlconfig import YMLConfig

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}


class StockNotifier:

    def __init__(self):
        self.config = YMLConfig().config
        self.telegram_bot = TelegramBot(self.config)

    def check(self):
        [self.check_inventories(url) for url in self.config['urls']]

    def check_inventories(self, url):
        page = requests.get(url, headers=HEADERS)

        if page.status_code != 200:
            self.telegram_bot.page_error(url, page.status_code)
        else:
            if self.is_in_stock(page.content):
                self.telegram_bot.in_stock(url)
            else:
                print('Out of Stock: {}'.format(url))

    def is_in_stock(self, html) -> bool:
        soup = BeautifulSoup(html, 'html.parser')
        button_disabled = soup.find("button", {'id': 'addToCartButton', 'disabled': True})
        return button_disabled is None
