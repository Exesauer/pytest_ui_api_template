import requests

class BoardApi:

    def __init__(self, token, api_key) -> None:
        self.base_url = "https://api.trello.com/1"
        self.token = token
        self.api_key = api_key

    def get_all_boards_by_org_id(self, org_id: str) -> dict:
        my_params = {
            'key': self.api_key,
            'token': self.token
            }
        path = f"{self.base_url}/organizations/{org_id}/boards"
        resp = requests.get(path, params=my_params)
        return resp.json()

    def create_board(self, name):
        my_params = {
            'name': name,
            'key': self.api_key,
            'token': self.token
            }
        path = f"{self.base_url}/boards/"
        resp = requests.post(path, params=my_params)
        return resp.json()