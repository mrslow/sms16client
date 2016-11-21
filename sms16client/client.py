# coding: utf-8

import requests
import md5
from exception import ApiException
from utils import find


class Client(object):

    BASE_URL = "https://new.sms16.ru/get"

    def __init__(self, login=None, api_key=None, sender=None):
        """
        Initialize with default vars. After initializing need to assign
        `login`,`api_key` and `sender`. See https://new.sms16.ru/api/
        """

        self.login = login
        self.api_key = api_key
        self.sender = sender

    @property
    def timestamp(self):
        """
        Getting UNIX timestamp
        :return: string
        """

        url = "{0}/{1}".format(self.BASE_URL, "timestamp.php")
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

        url = "{0}/{1}".format(self.BASE_URL, endpoint)
        params = {"login": self.login,
                  "timestamp": self.timestamp,
                  "return": "json"
                  }
        params.update(extra_params)
        signature = self.get_signature(params)
        params["signature"] = signature
        r = requests.get(url, params=params)
        response = r.json()
        error_code = find("error", response)
        if error_code:
            raise ApiException(error_code)
        return response


    def send(self, receivers, text):
        """
        Sending sms message.
        :param receivers: list of receiver's telephone numbers
        :param text: text message
        :return: dict
        """

        endpoint = "send.php"
        params = {"sender": self.sender,
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
