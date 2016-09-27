# coding: utf-8

import requests
import md5
from exception import ApiException

BASE_URL = "https://new.sms16.ru/get"

class Client(object):


    def __init__(self, login='', api_key=''):
        """
        Initialize with default vars. After initializing need to assign
        `login` and `api_key`. See https://new.sms16.ru/api/
        """

        self.login = login
        self.api_key = api_key

    @property
    def timestamp(self):
        """
        Getting UNIX timestamp
        :return: string
        """

        url = "{0}/{1}".format(BASE_URL, "timestamp.php")
        r = requests.get(url)
        return r.text

    def get_signature(self, params):
        """
        Create signature by params.
        :param params: dict with request parameters
        :return: string
        """

        string = ""
        for key in sorted(params):
            string += params[key]
        string += self.api_key
        m = md5.new(string.encode("utf-8"))
        return m.hexdigest()

    def request(self, endpoint, extra_params={}):
        """
        Make request by url. Getting data.
        :param endpoint: php script name on sms16.ru server
        :param extra_params: dict with request parameters
        :return: dict
        """

        url = "{0}/{1}".format(BASE_URL, endpoint)
        params = {"login": self.login,
                  "timestamp": self.timestamp,
                  "return": "json"
                  }
        params.update(extra_params)
        signature = self.get_signature(params)
        params["signature"] = signature
        r = requests.get(url, params=params)
        return r.json()


    def send(self, sender, receivers, text):
        """
        Sending sms message.
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
