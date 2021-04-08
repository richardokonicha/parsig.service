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
        url = f"{self.url}/apps"
        data={ "name" : name }
        app_response = requests.post(
        url=self.url,
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
        url = f"{self.url}/apps/{name}/builds"
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
            # "blob":{
            # "method": "put",
            # "url": "https://github.com/konichar/parsig"
            # }
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
    
    


herokuBridge = HerokuClient(URL, TOKEN, headers)
result = herokuBridge.create_builds("parsig2")

# result = configure_app(headers, "parsig2")
# result = info_app(headers, "parsig2")
# result = delete_app(headers, "parsig2")
# result = create_app(headers, "parsig2")
# result = get_apps(headers)

pprint(result)

# {'acm': True,
#  'archived_at': None,
#  'build_stack': {'id': '2be35cd6-418a-417e-9531-42c5de1dfb96',
#                  'name': 'heroku-20'},
#  'buildpack_provided_description': 'Python',
#  'created_at': '2021-03-17T10:14:19Z',
#  'git_url': 'https://git.heroku.com/eb2010-a.git',
#  'id': 'e539a23f-8aa3-4490-9414-ade2d494d425',
#  'internal_routing': None,
#  'maintenance': False,
#  'name': 'eb2010-a',
#  'organization': None,
#  'owner': {'email': 'emanuelebraha@gmail.com',
#            'id': '20d4b6f2-419a-4e2a-a38e-66974915dc5e'},
#  'region': {'id': '59accabd-516d-4f0e-83e6-6e3757701145', 'name': 'us'},
#  'released_at': '2021-04-05T07:47:51Z',
#  'repo_size': None,
#  'slug_size': 57500639,
#  'space': None,
#  'stack': {'id': '2be35cd6-418a-417e-9531-42c5de1dfb96', 'name': 'heroku-20'},
#  'team': None,
#  'updated_at': '2021-04-05T07:47:51Z',
#  'web_url': 'https://eb2010-a.herokuapp.com/'}