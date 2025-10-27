class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def wait_for(self, locator, timeout=10000):
        self.page.wait_for_selector(locator, timeout=timeout)

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()