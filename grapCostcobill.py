from splinter import Browser


def get_bill_number(browser):
    browser.visit('http://www.capitalone.ca/mycard')
    button = browser.find_by_text('Login')
    button.click()
