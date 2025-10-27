from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_invalid_password(page):
    base_url = "https://tester.codersguru.pl/"

    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.goto(base_url)

    home_page.go_to_login_page()
    login_page.login("aaaaa@wp.pl", "invalid")

    assert login_page.get_error_message() == "Nieprawidłowe dane."