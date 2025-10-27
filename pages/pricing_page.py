from pages.base_page import BasePage

class PricingPage(BasePage):
    
    PRICING_MENU = "//div[@class='header__menu-container']//a[@href='/cennik']"

    PAGE_HEADER = "//h1[contains(@class, 'pricing__header')]"

    CONSULTATION_PRICE = "//h2[contains(@class, 'pricing__subheader--green')]"

    def open_pricing_page(self):
        self.click(self.PRICING_MENU)

    def get_page_header(self):
        return self.page.locator(self.PAGE_HEADER).inner_text()

    def get_consultation_price(self):
        return self.page.locator(self.CONSULTATION_PRICE).inner_text()