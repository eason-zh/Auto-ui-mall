from time import sleep
import allure
from selenium.webdriver.common.by import By
from common.log import log


class Event:
    @staticmethod
    @allure.step("登录")
    def event_login(driver,username,password):
        try:
            sleep(1)
            driver.sel_click((By.XPATH,"//div[@class='tabbar']//div[4]"))
            driver.sel_send_keys((By.XPATH,"//input[@placeholder='请输入手机号码']"),username)
            driver.sel_send_keys((By.XPATH,"//input[@placeholder='请输入密码']"),password)
            driver.sel_click((By.XPATH,"//button[@type='submit']"))
        except Exception as e:
            log.error(e)
            raise e
