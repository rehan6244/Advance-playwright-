"""The Test Script (Abstraction & Assertions)

The test is clean, readable, and only uses business 
logic methods provided by the Page Object fixture. """


# tests/test_login_flow.py
import pytest

# Note: The LoginPage class is NOT imported here, only the fixture!

def test_successful_login(login_page):
    """
    Test reads like a user story, using only high-level actions.
    The test asserts the outcome.
    """
    # 🔑 Abstraction: The test only uses high-level, business-focused methods.
    login_page.login("valid_user", "secure_password")
    
    # Assertions: We verify the outcome here, not in the POM.
    # We expect the URL to change to the dashboard.
    assert "dashboard" in login_page.page.url
    
def test_invalid_credentials_shows_error(login_page):
    """
    Tests the error case using the encapsulated POM methods.
    """
    # 🔑 Abstraction: Perform the action
    login_page.login("invalid_user", "wrong_password")
    
    # Assertions: Verify the error message is correct.
    # The test calls the POM to retrieve the result state.
    expected_error = "Invalid username or password"
    actual_error = login_page.get_error_message()
    
    assert expected_error == actual_error
