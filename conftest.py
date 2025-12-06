""" This fixture ensures the LoginPage is 
correctly set up for every test that requests it,
handling the Page object initialization from Pytest."""

# conftest.py (or fixtures file)
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def playwright_instance():
    """Initializes Playwright."""
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def page(playwright_instance):
    """Provides a fresh Playwright page for each test."""
    browser = playwright_instance.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()

@pytest.fixture(scope="function")
def login_page(page):
    """
    Fixture for the LoginPage POM.
    This injects the Page Object into the test function.
    """
    login_page = LoginPage(page)
    login_page.navigate()
    return login_page
