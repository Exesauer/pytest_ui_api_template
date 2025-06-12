import requests

class BoardApi:

    def __init__(self, token, api_key) -> None:
        self.base_url = "https://api.trello.com/1"
        self.token = token
        self.api_key = api_key

    def get_all_boards_by_org_id(self, org_id: str) -> list:
        query = {
            'key': self.api_key,
            'token': self.token
            }
        path = f"{self.base_url}/organizations/{org_id}/boards"
        response = requests.get(path, params=query)
        return response.json()

    def create_board(self, name, defaultLists) -> dict:
        query = {
            'name': name,
            'key': self.api_key,
            'token': self.token,
            'defaultLists': defaultLists
            }
        path = f"{self.base_url}/boards/"
        response = requests.post(path, params=query)
        return response.json()
    
    def delete_board(self, id) -> requests.Response:
        query = {
            'key': self.api_key,
            'token': self.token
            }
        path = f"{self.base_url}/boards/{id}"
        response = requests.delete(path, params=query)
        return response
    
    def get_id_last_board(self, org_id: str) -> str:
        query = {
            'key': self.api_key,
            'token': self.token
            }
        path = f"{self.base_url}/organizations/{org_id}/boards"
        response = requests.get(path, params=query)
        return response.json()[-1]["id"]