""" This class hides the location of the elements and the methods needed to interact with them."""

# pages/login_page.py
from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)

class LoginPage:
    """Encapsulates the login page elements and actions."""
    
    # 🔒 Encapsulated Locators (Internal Details)
    _USERNAME_INPUT = "input[name='username']"
    _PASSWORD_INPUT = "input[name='password']"
    _LOGIN_BUTTON = "button:has-text('Login')"
    _ERROR_MESSAGE = "div[role='alert']"
    
    def __init__(self, page: Page):
        # The Playwright page object is encapsulated here
        self.page = page
        
    def navigate(self):
        """Action: Navigates to the login page."""
        self.page.goto("https://www.example.com/login")
        logger.info("Navigated to Login Page.")
        
    def login(self, username, password):
        """
        Action (Abstraction): Hides the click and fill logic.
        """
        logger.info(f"Attempting login for user: {username}")
        self.page.fill(self._USERNAME_INPUT, username)
        self.page.fill(self._PASSWORD_INPUT, password)
        self.page.click(self._LOGIN_BUTTON)
        # We do NOT assert here. We only perform the action.
        
    def get_error_message(self) -> str:
        """Action: Retrieves the current error message."""
        # Use Playwright's getByRole for Senior-level reliability
        error_element = self.page.get_by_role("alert", exact=True)
        return error_element.inner_text()
