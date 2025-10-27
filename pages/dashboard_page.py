from pages.base_page import BasePage

class DashboardPage(BasePage):
    USER_ICON = "//img[@class='settings-image']"

    def is_user_logged_in(self):
        self.wait_for(self.USER_ICON)
        return self.is_visible(self.USER_ICON)