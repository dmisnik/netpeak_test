import string    
import random
from BasePage import BasePage
from Locators import Locators

class Pages(BasePage):

    def click_about_us_button(self):
        self.find_element(Locators.LOCATOR_ABOUT_US_BUTTON).click()

    def click_team_button(self):
        self.find_element(Locators.LOCATOR_TEAM_BUTTON).click()

    def click_join_team_button(self):
        self.find_element(Locators.LOCATOR_JOIN_TEAM).click()

    def click_want_to_work_netpeak_button(self):
        self.find_element(Locators.LOCATOR_WANT_TO_WORK_IN_NETPEAK).click()

    def click_user_cabinet_button(self):
        self.find_element(Locators.LOCATOR_USER_CABINET).click()

    def click_enter_cabinet_button(self):
        self.find_element(Locators.LOCATOR_ENTER_CABINET).click()

    def check_button_disabled(self):
        assert not self.find_element(Locators.LOCATOR_ENTER_CABINET).is_enabled()

    def enter_random_creds_login_pass(self):
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
        login_field = self.find_element(Locators.LOCATOR_LOGIN_FIELD)
        login_field.send_keys(ran)
        pass_field = self.find_element(Locators.LOCATOR_PASS_FIELD)
        pass_field.send_keys(ran)

    def click_rules_checkbox(self):
        self.find_element(Locators.LOCATOR_CHECKBOX_CABINET).click()

    def check_alert_message(self):
        self.find_element(Locators.LOCATOR_ALERT_MESSAGE)

    def check_red_login_pass_color(self):
        errors = self.find_elements(Locators.LOCATOR_LOGIN_PASS_ALERT_RED)
        if len(errors) != 2:
            raise Exception


