# ===================================== #
# Fixtures
# Ref: https://playwright.dev/python/docs/test-configuration
# Ref: https://playwright.dev/python/docs/test-runners
# Ref: https://playwright.dev/docs/test-fixtures (not written for python yet)
# ===================================== #
import time
import pytest


EXECUTION_TIME = time.strftime('%Y-%m-%d_%H-%M-%S')


@pytest.fixture(scope="session")
def browser_context_args(playwright):
    ## Ref: https://playwright.dev/python/docs/api/class-browsertype
    # ----------------------
    # 📱 Phones
    #----------------------
    # Android Devices
    # ----------------------
    # "Galaxy Note 3"
    # "Galaxy Note II"
    # "Galaxy S III"
    # "Galaxy S5"
    # "Galaxy S8"
    # "Galaxy S9+"
    # "Nexus 4"
    # "Nexus 5"
    # "Nexus 5X"
    # "Nexus 6"
    # "Nexus 6P"
    # "Nexus 7"
    # "Pixel 2"
    # "Pixel 2 XL"
    # "Pixel 5"
    # ----------------------
    # iOS Devices
    # ----------------------
    # "iPhone 6"
    # "iPhone 6 landscape"
    # "iPhone 7"
    # "iPhone 7 landscape"
    # "iPhone 8"
    # "iPhone 8 landscape"
    # "iPhone SE"
    # "iPhone SE landscape"
    # "iPhone X"
    # "iPhone X landscape"
    # "iPhone 11"
    # "iPhone 11 Pro"
    # "iPhone 11 Pro Max"
    # "iPhone 12"
    # "iPhone 12 Pro"
    # "iPhone 13"
    # "iPhone 13 Pro"
    # "iPhone 14"
    # "iPhone 14 Pro"
    # "iPhone XR"
    # ----------------------
    # 📱 Tablets
    # ----------------------
    # Android Tablets
    # ----------------------
    # "Nexus 9"
    # "Nexus 10"
    # ----------------------
    # iPads
    # ----------------------
    # "iPad landscape"
    # "iPad Mini"
    # "iPad Mini landscape"
    # "iPad Pro 11"
    # "iPad Pro 11 landscape"
    # ----------------------
    # 🖥️ Desktops (emulated)
    # ----------------------
    # "Desktop Chrome"
    # "Desktop Firefox"
    # "Desktop Safari"
    # ----------------------
    ## Ref: https://playwright.dev/python/docs/emulation
    # Example:
    ## iphone_11 = playwright.devices["Galaxy S9+"]
    return {
        # **iphone_11,
        "is_mobile": True,
        "viewport": {
            "width": 1280, 
            "height": 720,
        },
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
def page(browser, browser_context_args, request):
    context = browser.new_context(**browser_context_args)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page
    context.tracing.stop(path=f"traces/{EXECUTION_TIME}/trace-{request.node.name}.zip")
    context.close()