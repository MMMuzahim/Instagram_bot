from time import sleep
from selenium import webdriver

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        browser.get('https://www.instagram.com/')


    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)
        self.browser.find_element_by_xpath('//button[normalize-space()="Not Now"]').click()

        return TapePage(self.browser)


class TapePage:
    def __init__(self, browser):
        self.browser = browser


    def is_liked(self, n):
        like_button_xpath = "/html/body/div[1]/section/main/section/div[1]/div[1]/div/article[" + str(n) + "]/div[2]/section[1]/span[1]/button"
        like_button = self.browser.find_element_by_xpath(like_button_xpath)
        svg = like_button.find_element_by_tag_name('svg')
        if svg.get_attribute('aria-label') == 'Like':
            return False
        return True


    def like_picture(self, n):
        like_button_xpath = "/html/body/div[1]/section/main/section/div[1]/div[1]/div/article[" + str(n) + "]/div[2]/section[1]/span[1]/button"
        if not (self.is_liked(n)):
            self.browser.find_element_by_xpath(like_button_xpath).click()
            sleep(2)
