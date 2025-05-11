import pytest
from playwright.sync_api import Page, expect

# ===================================== #
# Fixtures
# Ref: https://playwright.dev/python/docs/test-configuration
# ===================================== #
@pytest.fixture(scope="session")
def browser_context_args(playwright):
    ## Ref: https://playwright.dev/python/docs/api/class-browsertype
    ## Ref: https://playwright.dev/python/docs/emulation
    # iphone_11 = playwright.devices["iPhone 11 Pro"]
    return {
        "is_mobile": False,
        "viewport": {
            "width": 1280, 
            "height": 720,
        },
        # **iphone_11,
        "accept_downloads": False,
        "ignore_https_errors": True,
        "locale": "en-US",
        "timezone_id":"Asia/Baku",
        "geolocation": {
            "longitude": 13.4050,
            "latitude": 52.5200
        },
        "permissions": ["geolocation"],
    }

@pytest.fixture
def page(browser, browser_context_args):
    context = browser.new_context(**browser_context_args)
    page = context.new_page()
    yield page
    context.close()

# ===================================== #
# Variables
# ===================================== #
START_URL = "https://www.saucedemo.com/"
LOGIN_USERNAME = "standard_user"
LOGIN_PASSWORD = "secret_sauce"

# ===================================== #
# Locators
# Ref: https://playwright.dev/python/docs/locators
# ===================================== #
AUTH_USERNAME_LOCATOR = "input#user-name"
AUTH_PASSWORD_LOCATOR = "input#password"
AUTH_LOGIN_BTN_LOCATOR = "input#login-button"
PRODUCTS_PAGE_TITLE_LOCATOR = "span[data-test=\"title\"]"

# ===================================== #
# Tests
# ===================================== #
@pytest.mark.tags("JIRA-0001", "ui", "auth")
def test_user_should_be_logged_in_successfully(page: Page):
    page.goto(START_URL)
    page.locator(AUTH_USERNAME_LOCATOR).fill(LOGIN_USERNAME)
    page.locator(AUTH_PASSWORD_LOCATOR).fill(LOGIN_PASSWORD)
    page.locator(AUTH_LOGIN_BTN_LOCATOR).click()

    # Auto waiting
    # -------------
    # Ref: https://playwright.dev/python/docs/actionability
    page.locator(PRODUCTS_PAGE_TITLE_LOCATOR).wait_for(state="visible", timeout=5000) # Explicit wait 
    page.wait_for_timeout(2000) # Explicit wait for 2 seconds (delay)
    
    # Assertions
    # -----------
    # Ref: https://playwright.dev/python/docs/test-assertions
    expect(page.locator(PRODUCTS_PAGE_TITLE_LOCATOR)).to_have_text("Products")
    expect(page).to_have_title("Swag Labs")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")