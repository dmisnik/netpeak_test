from selenium.webdriver.common.by import By

class Locators:
    LOCATOR_ABOUT_US_BUTTON = (By.XPATH, "//li[@data-content='58']")
    LOCATOR_TEAM_BUTTON = (By.LINK_TEXT, "Команда")
    LOCATOR_JOIN_TEAM = (By.LINK_TEXT, "Стать частью команды")
    LOCATOR_WANT_TO_WORK_IN_NETPEAK = (By.LINK_TEXT, "Я хочу работать в Netpeak")
    LOCATOR_USER_CABINET = (By.LINK_TEXT, "Личный кабинет")
    LOCATOR_LOGIN_FIELD = (By.ID, "login")
    LOCATOR_PASS_FIELD = (By.ID, "password")
    LOCATOR_ENTER_CABINET = (By.CSS_SELECTOR, ".enter.md-button.md-ink-ripple")
    LOCATOR_CHECKBOX_CABINET = (By.CSS_SELECTOR, ".gdpr.ng-pristine.ng-untouched.ng-valid.ng-empty")
    LOCATOR_ALERT_MESSAGE = (By.CSS_SELECTOR, ".md-toast-text.ng-binding")
    LOCATOR_LOGIN_PASS_ALERT_RED = (By.CSS_SELECTOR, ".ng-pristine.md-input.ng-empty.ng-invalid.ng-invalid-required.ng-invalid-validation-error.ng-touched")