import json
from resources.urls import API_URL
from utils.request import APIRequest
from tests.helpers.get_token import get_token


def user_exists(user_list, new_user):
    for user in user_list:
        if user == new_user:
            return True
        else:
            return False


class UserClient:
    def __init__(self):
        self.api_url = API_URL
        self.request = APIRequest()
        self.token = get_token()
        self.head = {"Content-Type": "application/json", "Token": self.token}

    def create_user(self, body):
        new_username = body["username"]
        all_users = self.show_all_users().as_dict["payload"]
        if user_exists(all_users, new_username):
            print("User already exists.")
        else:
            response = self.request.post(self.api_url + "users",
                                         payload=json.dumps(body),
                                         headers=self.head)
            return response

    def update_user(self, info):
        if "username" in info.keys():
            target_user = info["username"]
            info.pop("username", None)
            info.pop("password", None)
        else:
            raise Exception("No username specified.")

        response = self.request.put(self.api_url + "users/" + target_user,
                                    payload=json.dumps(info),
                                    headers=self.head)
        return response

    def get_user_info(self, username):

        response = self.request.get(self.api_url + "users/" + username, **self.head)
        return response.as_dict["payload"]

    def show_all_users(self):
        response = self.request.get(self.api_url + "users")
        return response
