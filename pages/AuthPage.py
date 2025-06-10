from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3FreturnUrl%3D%252Fu%252Fexesauer%252Fboards%26display%3D%26aaOnboarding%3D%26updateEmail%3D%26traceId%3D%26ssoVerified%3D%26createMember%3D%26jiraInviteLink%3D"
        self.__driver = driver

    def go_atlassian_login(self):
        self.__driver.get(self.__url)
    
    def login_as(self, email: str, password: str):
        self.__driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
        self.__driver.find_element(By.CLASS_NAME, "css-178ag6o").click()
        password_element = WebDriverWait(self.__driver, 10).until(
             EC.visibility_of_element_located((By.CSS_SELECTOR, "#password")))
        password_element.send_keys(password)
        self.__driver.find_element(By.CLASS_NAME, "css-178ag6o").click()
        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "DD3DlImSMT6fgc")))

    def get_current_url(self):
        return self.__driver.current_url