import time
from splinter import Browser

import constants
import fileUtils


def get_bill_number():
    profile = fileUtils.getBroswerProfile()
    with Browser(profile_preferences=profile) as browser:
        browser.visit('http://www.capitalone.ca/mycard')
        browser.find_by_id('userid1').fill(constants.COSTCO_ACCOUNT)
        browser.find_by_id('password1').fill(constants.COSTCO_PASSWORD)
        browser.find_by_name('button1').click()
        value = browser.find_by_id('accountOverview').find_by_tag('table')[2].find_by_tag('tr').first.find_by_tag('td').last.value
        datelinkvalue = browser.find_by_id('accountOverview').find_by_tag('table')[2].find_by_tag('tr').first.find_by_tag('td')[1].value
        datelinkvalue = datelinkvalue.split('/')
        datelinkvalue = [datelinkvalue[2], datelinkvalue[1], datelinkvalue[0]]
        datelinkvalue = fileUtils.seperate_with(datelinkvalue)
        browser.find_by_text('Statements').click()
        browser.find_by_text('Historical Statements').click()
        browser.find_by_text('View, print or save Complete Statement').click()
        time.sleep(5)
        fileUtils.renameFile('CapitalOne_'+datelinkvalue+'.pdf')
        return value

if __name__ == '__main__':
    print('Costco bill: ', get_bill_number())