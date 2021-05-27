import requests


class TelegramBot:

    def __init__(self, config):
        self.token = config['telegram']['token']
        self.chats = config['telegram']['chats']

    def in_stock(self, url: str):
        message = 'In Stock: {}'.format(url)
        self.__send_message(message)

    def page_error(self, url, status_code):
        message = 'Error on page: {} \n Status: {}'.format(url, status_code)
        self.__send_message(message)

    def __send_message(self, message):
        for chat in self.chats:
            message_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&parse_mode=Markdown&text={}'.format(
                self.token, chat, message)
            requests.get(message_url)
