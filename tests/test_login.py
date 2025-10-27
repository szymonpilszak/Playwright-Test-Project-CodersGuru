"""
Login tests for the tester.codersguru.pl application.

This module contains functional tests for the login functionality using
the Page Object Pattern with Playwright and pytest

Tests include:
- Successful login (test_login_positive)
- Invalid login attempts with parameterization (test_login_invalid)
"""

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

base_url = "https://tester.codersguru.pl/"



def test_login_positive(page): 
    """
    Test a successful login.

            Steps:
            1. Navigate to the home page.
            2. Go to the login page.
            3. Enter valid credentials.
            4. Assert that the user is logged in successfully.
    """

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
    Test login with invalid credentials.

            Steps:
            1. Navigate to the home page.
            2. Go to the login page.
            3. Attempt login with invalid credentials.
            4. Assert that the appropriate error message is displayed.
    """
    home = HomePage(page)
    login = LoginPage(page)

    home.goto(base_url)
    home.go_to_login_page()
    login.login(username, password)

    assert login.get_error_message() == "Nieprawidłowe dane."