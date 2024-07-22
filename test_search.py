from selene import browser, be, have


def test_something(w_size):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_something2(w_size):
    browser.element('[name="q"]').should(be.blank).type('tyuudjjj222').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу tyuudjjj222 ничего не найдено. '))
