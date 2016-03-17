# coding: utf-8

import requests
import md5

BASE_URL = 'https://new.sms16.ru/get'
ERRORS = {
    0: u'Сервис отключен',
    1: u'Не указана подпись',
    2: u'Не указан логин',
    3: u'Не указан текст',
    4: u'Не указан телефон',
    5: u'Не указан отправитель',
    6: u'Некорректная подпись',
    7: u'Некорректный логин',
    8: u'Некорректное имя отправителя',
    9: u'Незарегистрированное имя отправителя',
    10: u'Не одобренное имя отправителя',
    11: u'В тексте содержатся запрещенные слова',
    12: u'Ошибка отправки СМС',
    13: u'Номер находится в стоп-листе. Отправка на этот номер запрещена',
    14: u'В запросе более 50 номеров',
    15: u'Не указана база',
    16: u'Некорректный номер',
    17: u'Не указаны ID СМС',
    18: u'Не получен статус',
    19: u'Пустой ответ',
    20: u'Номер уже существует',
    21: u'Отсутствует название',
    22: u'Шаблон уже существует',
    23: u'Не указан месяц (Формат: YYYY-MM)',
    24: u'Не указана временная метка',
    25: u'Ошибка доступа к базе',
    26: u'База не содержит номеров',
    27: u'Нет валидных номеров',
    28: u'Не указана начальная дата',
    29: u'Не указана конечная дата',
    30: u'Не указана дата (Формат: YYYY-MM-DD)',
}

class Sms16Client(object):

    def __init__(self):
        """
        Initialize with default vars. After initializing need to assign
        `login` and `api_key`. See https://new.sms16.ru/api/
        """

        self.login = ''
        self.api_key = ''
        self.host = BASE_URL
        self.errors = ERRORS

    def send(self, sender, receivers, text):
        """
        Sending sms message
        :param sender: name of sender
        :param receivers: list of receiver's telephone numbers
        :param text: text message
        :return: dict
        """

        endpoint = "send.php"
        params = {"sender": sender,
                  "phone": ','.join(receivers),
                  "text": text
                  }
        return self.request(endpoint, params)

    def balance(self):
        """
        Getting account balance.
        :return: dict
        """

        endpoint = "balance.php"
        return self.request(endpoint)

    def status(self, states):
        """
        Getting status of sended messages.
        :param states: list of sended messages id
        :return: dict
        """

        endpoint = "status.php"
        params = {"state": ",".join(states)}
        return self.request(endpoint, params)

    def signature(self, params):
        """
        Create signature by params.
        :param params: dict with request parameters
        :return: string
        """

        string = ""
        for key in sorted(params):
            string += params[key]
        string += self.api_key
        m = md5.new(string)
        return m.hexdigest()

    def timestamp(self):
        """
        Getting UNIX timestamp
        :return: string
        """

        url = "{0}/{1}".format(self.host, "timestamp.php")
        r = requests.get(url)
        return r.text

    def request(self, endpoint, extra_params={}):
        """
        Make request by url. Getting data.
        :param endpoint: php script name on sms16.ru server
        :param extra_params: dict with request parameters
        :return: dict
        """

        url = "{0}/{1}".format(self.host, endpoint)
        params = {"login": self.login,
                  "timestamp": self.timestamp(),
                  "return": "json"
                  }
        params.update(extra_params)
        signature = self.signature(params)
        params["signature"] = signature
        r = requests.get(url, params=params)
        return r.json()
