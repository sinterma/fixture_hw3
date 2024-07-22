import pytest
from selene import browser


@pytest.fixture(scope="function")
def w_size():
    browser.config.window_height = 1200
    browser.config.window_width = 1200
    browser.open('https://google.com')

    yield

    browser.quit()
