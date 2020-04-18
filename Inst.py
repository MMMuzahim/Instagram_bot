from time import sleep
from selenium import webdriver
from pages import LoginPage
from selenium.webdriver.common.keys import Keys


username = input('Input username: ')
password = input('Input password: ')

browser = webdriver.Firefox()
browser.implicitly_wait(5)

login_page = LoginPage(browser)
tape_page = login_page.login(username, password)

n = 1
while True:
    try:
        tape_page.like_picture(n)
        n += 1
    except Exception:
        n=1
        browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

browser.close()
