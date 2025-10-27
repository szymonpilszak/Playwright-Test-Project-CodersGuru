from pages.base_page import BasePage

class HomePage(BasePage):
    LOGIN_BUTTON = "//button[contains(@class, 'header__button') and not(contains(@class, 'header__button-mobile'))]"
    REGISTER_BUTTON = "//input[@type='submit' and @value='Załóż konto']"

    def go_to_login_page(self):
        self.click(self.LOGIN_BUTTON)

    def go_to_register_page(self):
        self.click(self.REGISTER_BUTTON)