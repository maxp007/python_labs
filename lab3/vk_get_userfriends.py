import requests
import datetime
import json
from base_client import BaseClient


class VkUserFriends(BaseClient):
    BASE_URL = "https://api.vk.com/"
    http_method = "?"

    def __init__(self, user_id):
        self.params = {"user_id": str(user_id), "fields": "bdate", "access_token": "", "v": "5.68"}
        self.user_id = user_id
        self.method = "method/friends.get"
        self.response_content = ""
        self.dates_list = []
        self.ages_list = []
        self.response = requests.Response()

    def get_params_string(self):
        params_string = ""
        for key, value in self.params.items():
            params_string = params_string + key + "=" + value + "&"
        return params_string

    def _get_data(self, method, http_method):
        response = requests.Response()
        print(self.BASE_URL + self.method + self.http_method + self.get_params_string())
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
            for el in data["response"]["items"]:
                if "bdate" in el:
                    self.dates_list.append(el.get("bdate", "None"))
        except KeyError:
            print("Invalid user domain")
            exit(1)

        date_obj_list = []
        for dates in self.dates_list:
            try:
                date_obj_list.append(datetime.datetime.strptime(dates, "%d.%m.%Y"))
            except ValueError:
                pass

        for obj in date_obj_list:
            age = int((datetime.datetime.now()-obj).days // 365.25)
            self.ages_list.append(age)
        return self.ages_list

    def get_headers(self):
        return self.response.headers()

    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )