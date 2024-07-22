from selene import browser, be, have, by


def test_something(w_size):
    browser.open('https://google.com')
    if browser.element(by.text('Accept All')).matching(be.visible):
        browser.element(by.text('Accept All')).click()
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_something2(w_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('tyuudjjj222').press_enter()
    browser.element('[id="botstuff"]').should(have.text('Your search - tyuudjjj222 - did not match any documents.git rm -r --cached .idea'))
