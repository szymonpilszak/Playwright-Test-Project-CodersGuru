from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_success(page):
    base_url = "https://tester.codersguru.pl/"

    home_page = HomePage(page)
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    home_page.goto(base_url)
    home_page.go_to_login_page()
    login_page.login("aaaaa@wp.pl", "aaaaa")

    assert dashboard_page.is_user_logged_in(), "Login failed!"