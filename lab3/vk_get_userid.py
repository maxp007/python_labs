import requests
import datetime
import json
from base_client import BaseClient


class VkUserId(BaseClient):
    BASE_URL = "https://api.vk.com/"
    http_method = "?"

    def __init__(self, user_domain):
        self.params = {"user_ids": user_domain, "fields": "bdate", "access_token": "", "v": "5.68" }
        self.user_domain = user_domain
        self.method = "method/users.get"
        self.response = requests.Response()
        self.response_content = ""
        self.user_id = ""

    def get_params_string(self):
        params_string = ""
        for key, value in self.params.items():
             params_string = params_string + key + "=" + value + "&"
        return params_string

    def _get_data(self, method, http_method):
        response = requests.Response()
        print(self.BASE_URL + self.method + self.http_method + self.get_params_string())
        # Argument y in requests.get(x, y) is a dictionary of parameters
        try:
            response = requests.get(self.BASE_URL + self.method + self.http_method,  self.params)
        except ConnectionError:
            print("Ошибка соединения с сервером")
            exit(1)
        return self.response_handler(response)

    def response_handler(self, response):
        if response.status_code != 200:
            print("response :", response.status_code)
            exit(1)
        self.response = response
        self.response_content = response.content.decode("utf-8")
        data = json.loads(self.response_content)
        try:
            self.user_id = data["response"][0]["id"]
        except KeyError:
            print("Invalid user domain")
            exit(1)
        return None

    def get_headers(self):
        return self.response.headers()

    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )

