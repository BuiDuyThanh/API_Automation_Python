import requests
import json
from requests.auth import HTTPBasicAuth
from resources.urls import API_URL


def get_token():
    response = requests.get(API_URL + "auth/token", auth=HTTPBasicAuth("user1", "123456789"))
    token = json.loads(json.dumps(response.json(), indent=4))["token"]
    return token
