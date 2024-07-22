import pytest
from selene import browser


@pytest.fixture(scope="function")
def w_size():
    browser.config.base_url = 'https://google.com'
    browser.config.window_height = 1200
    browser.config.window_width = 1200
    yield

    browser.quit()
