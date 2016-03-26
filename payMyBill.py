import time
from splinter import Browser

import constants
import fileUtils
import grapCostcobill
import grapGasbill
import grapMBNAbill


def login_rbc():
    profile = fileUtils.getBroswerProfile()
    with Browser(profile_preferences=profile) as browser:
        browser.visit('http://www.rbc.com/canada.html')
        browser.find_by_text('Sign In ').click()
        browser.find_by_id('K1').fill(constants.RBC_ACCOUNT)
        browser.find_by_id('Q1').fill(constants.RBC_PASSWORD)
        browser.find_by_text('Sign In').click()
        browser.click_link_by_partial_text('RBC Shoppers Optimum')
        value = browser.find_by_xpath('''//tr[@class='ccadTableBold']''').last.find_by_tag('td').value
        return value



if __name__ == '__main__':
    # print('MBNA', grapMBNAbill.get_bill_number())
    # print('Costco', grapCostcobill.get_bill_number())
    # print('Enbridge', grapGasbill.get_bill_number())
    print('RBC Credit card', login_rbc())