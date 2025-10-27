import pytest
from pages.base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    USERNAME_INPUT = "//input[@id='username']"
    PASSWORD_INPUT = "//input[@id='password']"
    SUBMIT_BUTTON = "//button[@id='_submit']"
    MISSING_CREDENTIALS_ERROR_MESSAGE = "//span[contains(@class,'form-error') and text()='To pole jest wymagane']"

    def login(self, username, password):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)
    
    
    def click_submit(self):
        self.click(self.SUBMIT_BUTTON)
        
        
    def get_invalid_credentials_error_message(self):
        return self.page.locator(".db-info").inner_text()
    
    def get_missing_credentials_error_message(self):
        expect(self.page.locator(self.MISSING_CREDENTIALS_ERROR_MESSAGE)).to_be_visible()