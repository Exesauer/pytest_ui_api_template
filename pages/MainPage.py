import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__(self, driver: WebDriver)->None:
        self.__driver = driver

    @allure.step("Переход на страницу Trello")
    def go_trello(self):
        element = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Trello']")))
        element.click()
        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-testid=header-member-menu-button]")))

    @allure.step("Отображение меню пользователя")
    def open_profile_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=header-member-menu-button]").click()

    @allure.step("Получение информации о пользователе")
    def get_account_info(self) -> list[str]:
        locator = (By.CSS_SELECTOR, "[data-testid=account-menu-account-section]")
        menu = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located(locator))
        name = menu.find_element(By.CSS_SELECTOR, ".lzFtVDCea8Z9jO").text
        email = menu.find_element(By.CSS_SELECTOR, ".Ej7WGzTnvdxL7I").text
        return [name, email]

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.__driver.current_url