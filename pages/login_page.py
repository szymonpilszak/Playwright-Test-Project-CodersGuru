from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = "//input[@id='username']"
    PASSWORD_INPUT = "//input[@id='password']"
    SUBMIT_BUTTON = "//button[@id='_submit']"

    def login(self, username, password):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)
        
        
    def get_error_message(self):
        return self.page.locator(".db-info").inner_text()