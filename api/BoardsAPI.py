import requests
import allure

class BoardApi:

    def __init__(self, base_url, api_key, token) -> None:
        self.base_url = base_url
        self.token = token
        self.api_key = api_key

    @allure.step("Получение всех досок по ID организации")
    def get_all_boards_by_org_id(self, org_id: str) -> list:
        query = {
            'key': self.api_key,
            'token': self.token
            }
        path = f"{self.base_url}/organizations/{org_id}/boards"
        response = requests.get(path, params=query)
        try:
            response.raise_for_status()
            result = response.json()
        except requests.exceptions.HTTPError as e:
            print(f"Произошла ошибка при выполнении запроса: {e}")
        return result

    @allure.step("Создание доски")
    def create_board(self, name, defaultLists) -> dict:
        query = {
            'name': name,
            'key': self.api_key,
            'token': self.token,
            'defaultLists': defaultLists
            }
        path = f"{self.base_url}/boards/"
        response = requests.post(path, params=query)
        try:
            response.raise_for_status()
            result = response.json()
            board_id = result.get("id", "ID не найден")
            allure.attach(body=board_id, name="ID созданной доски", attachment_type=allure.attachment_type.TEXT)
        except requests.exceptions.HTTPError as e:
            allure.attach(body=str(response.content), name="HTTPError Details", attachment_type=allure.attachment_type.TEXT)
            print(f"Произошла ошибка при выполнении запроса: {e}")
            result = {}
        return result

    @allure.step("Удаление доски по ID")
    def delete_board_by_id(self, id) -> dict:
        query = {
            'key': self.api_key,
            'token': self.token
            }
        path = f"{self.base_url}/boards/{id}"
        response = requests.delete(path, params=query)
        result = {}  # Инициализация переменной
        try:
            response.raise_for_status()
            # Проверяем присутствие тела ответа
            if response.content:
                result = response.json()
        except requests.exceptions.HTTPError as e:
            allure.attach(body=str(response.content), name="HTTPError Details", attachment_type=allure.attachment_type.TEXT)
            print(f"Произошла ошибка при выполнении запроса: {e}")
            result = None
        return result

    def get_id_last_board(self, org_id: str) -> str:
        return self.get_all_boards_by_org_id(org_id)[-1]["id"]