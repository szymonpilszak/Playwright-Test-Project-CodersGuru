import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

base_url = "https://tester.codersguru.pl/"

def test_login_positive(page):

    home_page = HomePage(page)
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    home_page.goto(base_url)
    home_page.go_to_login_page()
    login_page.login("aaaaa@wp.pl", "aaaaa")

    assert dashboard_page.is_user_logged_in(), "Login failed!"
    
    
    
    
@pytest.mark.parametrize("username,password", [
    ("invalid@test.pl", "aaaaa"),
    ("aaaaa@wp.pl", "invalid")
])
def test_login_invalid(page, username, password):
    """
    Sprawdza, że logowanie z nieprawidłowymi danymi wyświetla odpowiedni komunikat błędu.
    """
    home = HomePage(page)
    login = LoginPage(page)

    home.goto(base_url)
    home.go_to_login_page()
    login.login(username, password)

    assert login.get_error_message() == "Nieprawidłowe dane."