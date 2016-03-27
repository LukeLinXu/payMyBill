import time
from splinter import Browser

import constants
import fileUtils


def get_bill_number():
    profile = fileUtils.getBroswerProfile()
    with Browser(profile_preferences=profile) as browser:
        browser.visit('https://service.mbna.ca/waw/mbna/logon')
        browser.find_by_id('usernameInput').fill(constants.MBNA_ACCOUNT)
        browser.find_by_id('passwordInput').fill(constants.MBNA_PASSWORD)
        browser.find_by_id('login').click()
        if False:
            question = browser.find_by_id('MFAChallengeForm:question').value
            browser.find_by_id('MFAChallengeForm:answer').fill(constants.get_answer(question))
            browser.find_by_id('MFAChallengeForm:validateButton').click()
        time.sleep(5)
        browser.find_by_id('shortcuts0').find_by_tag('input').last.click()
        browser.find_by_tag('span').find_by_text('Statements').click()

        infos = browser.find_by_xpath('''//div[@class='td-layout-column td-layout-grid2 td-copy-align-right td-margin-none td-layout-column-last']''')

        value = infos[0].value
        datelinkvalue = infos[1].value
        # datelinkvalue = datelinkvalue.replace(' ', '')
        datelinkvalue = datelinkvalue.split('/')
        datelinkvalue = [datelinkvalue[2], datelinkvalue[0], datelinkvalue[1]]
        datelinkvalue = fileUtils.seperate_with(datelinkvalue)
        browser.find_by_text('Save current statement (pdf) ').click()
        time.sleep(5)
        fileUtils.renameFile('MBNA_'+datelinkvalue+'.pdf')
        return value

if __name__ == '__main__':
    print('MBNA bill: ', get_bill_number())




