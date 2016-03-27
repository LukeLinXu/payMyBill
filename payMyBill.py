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
    mbna = grapMBNAbill.get_bill_number()
    print('MBNA', mbna)
    costco = grapCostcobill.get_bill_number()
    print('Costco', costco)
    gas = grapGasbill.get_bill_number()
    print('Enbridge', gas)
    rbc = login_rbc()
    print('RBC Credit card', rbc)
    print('RRSP', '$100')
    print('Total will be: $', fileUtils.get_num(mbna)+fileUtils.get_num(costco)+fileUtils.get_num(gas)+fileUtils.get_num(rbc)+100)
