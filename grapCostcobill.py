from splinter import Browser


def get_bill_number():
    with Browser('chrome') as browser:
        browser.visit('http://www.capitalone.ca/mycard')
        button = browser.find_by_text('Login')
        button.click()


if __name__ == '__main__':
    get_bill_number()