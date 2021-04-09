import requests
import os
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()

URL = os.getenv("URL")
TOKEN = os.getenv("TOKEN")

headers={"Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/vnd.heroku+json; version=3"}


class HerokuClient:
    def __init__(self, url, token, headers):
        self.url = url
        self.token = token
        self.headers = headers


    def get_apps(self):
        url = f"{self.url}/apps"
        app_response = requests.get(
            url=self.url,
            headers=self.headers,
        ).json()
        return app_response

    def create_app(self, name):
        endpoint = f"{self.url}/apps/"
        data={ "name" : name }
        app_response = requests.post(
        url=endpoint,
        headers=self.headers,
        json=data
        ).json()
        return app_response

    def delete_app(self, name):
        url = f"{self.url}/apps/{name}"
        app_response = requests.delete(
            url=url,
            headers=self.headers,
        ).json()
        return app_response

    def info_app(self, name):
        url = f"{self.url}/apps/{name}/formation"
        app_response = requests.get(
            url=url,
            headers=self.headers,
        ).json()
        return app_response

    def create_slug(self, name):
        url = f"{self.url}/apps/{name}/slugs"
        data = {
            "process_types": {"worker":"python3 telethon_access.py"} ,
            'buildpack_provided_description': 'Python',
            }
        app_response = requests.post(
            url=url,
            headers=self.headers,
            body=data
        ).json()
        return app_response

    def create_release(self, name):
        url = f"{self.url}/apps/{name}/releases"
        data = {
            "slug": '8e258a29-e4c6-4bd8-afc0-bfd2f9203162',
            "description": "parsig release",
        }
        app_response = requests.post(
            url=url,
            headers=self.headers,
            json=data
        ).json()
        return app_response

    def create_builds(self, name):
        url = f"{self.url}/apps/{name}/builds"
        data = {
            "source_blob":{
                "url":"https://github.com/konichar/parsesig/archive/master.tar.gz", "version": "1"
                }
            }
        app_response = requests.post(
            url=url,
            headers=self.headers,
            json=data
        ).json()
        return app_response
    
    def create_formation(self, name):
        url = f"{self.url}/apps/{name}/formation/worker/"
        data = {
            "quantity": 1,
            # "size": "standard-1X"
            }
        app_response = requests.patch(
            url=url,
            headers=self.headers,
            json=data
        ).json()
        return app_response
    
    def set_config_vars(self, name):
        url = f"{self.url}/apps/{name}/config-vars/"
        data = {
            "API_HASH": "f36c296645a468c16a698ecb1e59e31b",
            "API_ID": "1271225",
            "CHATINPUT": "-1001434923897",
            "CHATOUTPUT": "https://t.me/TestAB21_bot",
            "SESSION": "1271225",
            }
        app_response = requests.patch(
            url=url,
            headers=self.headers,
            json=data
        ).json()
        return app_response
    


herokuBridge = HerokuClient(URL, TOKEN, headers)
result = herokuBridge.set_config_vars("parsig3")

pprint(result)