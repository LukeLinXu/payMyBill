from splinter import Browser


def get_bill_number(browser):
    browser.visit('https://www.mbna.ca/')
    button = browser.find_by_text('Log In')
    button.click()
