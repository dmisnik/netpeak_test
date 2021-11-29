from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://netpeak.ua/"

    def go_to_site(self):
        self.driver.get(self.base_url)

    def find_element(self, locator, time = 10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
        message = "Can't find element by locator")

    def find_elements(self, locator, time = 10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
        message = "Can't find any elements by locator")

    def switch_tab(self, tab):
        self.driver.switch_to.window(self.driver.window_handles[(tab)])

    def check_title(self, query):
        assert query in self.driver.title
