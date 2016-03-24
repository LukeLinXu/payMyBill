import time
from splinter import Browser


account = 'XXXXX'
password = 'XXXXXX'

def get_bill_number():
    with Browser('chrome') as browser:
        browser.visit('https://www.enbridgegas.com/myEnbridge/login.aspx')
        browser.find_by_id('ctl00_BodyContent_ctrlLogin1_login_UserName').fill(account)
        browser.find_by_id('ctl00_BodyContent_ctrlLogin1_login_Password').fill(password)
        button = browser.find_by_text('SIGN IN')
        button.click()
        browser.find_by_id('ctl00_ctl00_BodyContent_ContentPlaceHolder1_lnkViewCurrentBill').click()
        value = browser.find_by_id('ctl00_Main_lvBills_ctrl0_rptCatalog_ctl05_lblContent').value
        datelink = browser.find_by_id('ctl00_Main_lvBills_ctrl0_rptCatalog_ctl03_lnkFileLink')
        datelinkvalue = datelink.value
        datelink.click()
        browser.find_by_id('PDF').click()
        # prompt = browser.get_alert()
        # print(prompt.text)
        time.sleep(15)
        return value

if __name__ == '__main__':
    print('Enbridge bill: ', get_bill_number())