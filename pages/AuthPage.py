import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://id.atlassian.com/login?application=trello"
        self.__driver = driver

    @allure.step("Переход на страницу авторизации")
    def go_login_atlassian(self):
        self.__driver.get(self.__url)

    @allure.step("Ввод авторизационных данных")
    def login_as(self, email: str, password: str):
        self.__driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
        self.__driver.find_element(By.CLASS_NAME, "css-178ag6o").click()
        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#password"))).send_keys(password)
        self.__driver.find_element(By.CLASS_NAME, "css-178ag6o").click()

    def auth_check(self):
        greeting_element = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid=home-header-greeting]"))).text
        return greeting_element