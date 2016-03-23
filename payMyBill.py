from splinter import Browser

with Browser() as browser:
    url = "http://www.rbc.com/canada.html"
    browser.visit(url)
    button = browser.find_by_text('Sign In ')
    button.click()
    if browser.is_text_present('splinter.readthedocs.org'):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")   