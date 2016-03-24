import time
from splinter import Browser

import grapCostcobill
import grapMBNAbill


def login_rbc(browser):
    url = "http://www.rbc.com/canada.html"
    browser.visit(url)
    button = browser.find_by_text('Sign In ')
    button.click()
    time.sleep(50)



if __name__ == '__main__':
    with Browser('chrome') as browser:
        # grapMBNAbill.get_bill_number()
        # grapCostcobill.get_bill_number()
        login_rbc(browser)
