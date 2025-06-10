from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__(self, driver: WebDriver)->None:
        self.__driver = driver

    def get_current_url(self)->str:
        return self.__driver.current_url
    
    def open_profile_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=header-member-menu-button]").click()

    def get_account_info(self) -> list[str]:
        menu = self.__driver.find_element(By.CSS_SELECTOR, "[data-testid=account-menu-account-section]")
        name = menu.find_element(By.CSS_SELECTOR, ".lzFtVDCea8Z9jO").text
        email = menu.find_element(By.CSS_SELECTOR, ".Ej7WGzTnvdxL7I").text
        return [name, email]
