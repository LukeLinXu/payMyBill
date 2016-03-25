import time
from splinter import Browser

import constants
import fileUtils

def get_bill_number():
    profile = fileUtils.getBroswerProfile()
    with Browser(profile_preferences=profile) as browser:
        browser.visit('https://www.enbridgegas.com/myEnbridge/login.aspx')
        browser.find_by_id('ctl00_BodyContent_ctrlLogin1_login_UserName').fill(constants.ENBRIDGE_ACCOUNT)
        browser.find_by_id('ctl00_BodyContent_ctrlLogin1_login_Password').fill(constants.ENBRIDGE_PASSWORD)
        button = browser.find_by_text('SIGN IN')
        button.click()
        browser.find_by_id('ctl00_ctl00_BodyContent_ContentPlaceHolder1_lnkViewCurrentBill').click()
        value = browser.find_by_id('ctl00_Main_lvBills_ctrl0_rptCatalog_ctl05_lblContent').value
        datelink = browser.find_by_id('ctl00_Main_lvBills_ctrl0_rptCatalog_ctl03_lnkFileLink')
        datelinkvalue = datelink.value.replace('/', '_')
        datelink.click()
        browser.find_by_id('PDF').click()
        time.sleep(5)
        fileUtils.renameFile('Enbridge_'+datelinkvalue+'.pdf')
        return value

if __name__ == '__main__':
    print('Enbridge bill: ', get_bill_number())