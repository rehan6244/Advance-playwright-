Fixtures are the Glue: Pytest fixtures like login_page seamlessly provide the encapsulated Page Object to the test function, simplifying setup.

No Selectors in Tests: Notice that the test scripts contain zero CSS selectors, XPath, or Playwright interaction methods (.click(), .fill()). The test's only job is to describe what to do and assert what happened.

Encapsulation = Maintainability: If the website's login button selector changes, you only edit the _LOGIN_BUTTON locator in one spot (login_page.py). Every test that uses login_page.login() will continue to work without modification.
