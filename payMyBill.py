from splinter import Browser

import grapCostcobill
import grapMBNAbill


def login_rbc(browser):
    url = "http://www.rbc.com/canada.html"
    browser.visit(url)
    button = browser.find_by_text('Sign In ')
    button.click()



if __name__ == '__main__':
    with Browser() as browser:
        grapMBNAbill.get_bill_number(browser)
        grapCostcobill.get_bill_number(browser)
        login_rbc(browser)
