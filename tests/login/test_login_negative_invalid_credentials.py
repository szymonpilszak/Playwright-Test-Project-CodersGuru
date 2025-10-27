import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage



@pytest.mark.parametrize("username,password", [
    ("invalid@email.pl","aaaaa"),       # Invalid username, valid password
    ("aaaaa@wp.pl","invalidpassword"),  # Valid username, invalid password
])
def test_login_invalid_credentials(page, username, password):
    base_url = "https://tester.codersguru.pl/"

    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.goto(base_url)

    home_page.go_to_login_page()
    login_page.login("aaaaa@wp.pl", "invalid")

    assert login_page.get_error_message() == "Nieprawidłowe dane."