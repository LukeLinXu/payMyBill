from splinter import Browser


def get_bill_number():
    browser = Browser('chrome')
    browser.visit('https://www.mbna.ca/')
    button = browser.find_by_text('Log In')
    button.click()


if __name__ == '__main__':
    get_bill_number()