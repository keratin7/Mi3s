#python:
from selenium.webdriver import Chrome

YOUR_PAGE_URL = 'http://www.mi.com/in/events/diwali2016/'
NEXT_BUTTON_XPATH = '//*[@id="redmi"]/div/div/ul/li[1]/div[2]/a'
try:
    browser = Chrome()
    browser.get(YOUR_PAGE_URL)

    button = browser.find_element_by_xpath(NEXT_BUTTON_XPATH)
    button.click()
except AttributeError:
    pass