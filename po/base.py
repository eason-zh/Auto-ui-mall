import os
import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from time import sleep
import re
import allure
from selenium.webdriver.support.wait import WebDriverWait
from common.log import log
from config.conf import ALLURE_IMG_DIR


class Base:
    def __init__(self, driver=None):
        try:
            self.driver = driver or webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
        except Exception as e:
            log.error(f"初始化驱动失败：{e}")
            raise e


    def get(self,url):
        try:
            self.driver.get(url)
            return self.driver
        except Exception as e:
            raise e

    def quit(self):
        try:
            self.driver.quit()
        except Exception as e:
            raise e

    def  alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            log.info(f"Alert text: {text}")
            alert.accept()
            return text
        except Exception as e:
            raise e
    def click_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception as e:
            raise e

    @allure.step("鼠标左键点击")
    def sel_click(self,sel,timeout=20):
        try:
            ele=WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((sel)))
            ele.click()
            sleep(0.2)
            selen = re.sub('[^\u4e00-\u9fa5]+', '', str(sel))
            if len(selen) > 0:
                log.info(f"左键点击：{selen}")
            return True
        except Exception as e:
            log.error(f"定位失败：{sel}, 错误信息：{e}")
            raise e
    @allure.step("元素可点击")
    def element_clickable(self,by,sel,timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable((by, sel)))
            return True
        except Exception as e:
            log.error(f"以达到超时时间元素{sel}仍未加载出来，错误信息：{e}")
            raise e

    @allure.step("元素可见")
    def element_visible(self,sel,timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by,sel)))
            return True
        except Exception as e:
            log.error(f"以达到超时时间元素{sel}仍不可见，错误信息：{e}")
            raise e

    @allure.step("输入内容")
    def sel_send_keys(self,sel,value,timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(sel)).clear()
            sleep(0.2)
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(sel)).send_keys(value)
            sleep(0.2)
            selen = re.sub('[^\u4e00-\u9fa5]+', '', str(sel))
            if len(selen) > 0:
                log.info(f"输入内容：{selen}，内容：{value}")
            return True
        except Exception as e:
            log.error(f"输入内容失败：{sel}, 错误信息：{e}")
            raise e

    @allure.step("获取元素文本")
    def sel_get_text(self,sel,timeout=10,mode=0):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((sel)))
            if mode == 0:
                log.info(f"获取元素文本：{element.text}")
                return element.text
            elif mode == 1:
                log.info(f"获取元素属性：{element.get_attribute('value')}")
                return element.get_attribute("value")
        except Exception as e:
            log.error(f"获取元素文本失败：{sel}, 错误信息：{e}")
            return None

    def allure_save_screenshot(self,name):
        with open(self.chrom_save_screenshot(),"rb") as f:
            allure.attach(f.read(),name,attachment_type=allure.attachment_type.JPG)

    @allure.step("获取截图")
    def chrom_save_screenshot(self):
        try:
            img_dir = ALLURE_IMG_DIR
            str_time = str(time.time())[:10]
            img_file = ALLURE_IMG_DIR + f'//tem_chrom_save_screenshot{str_time}.jpg'
            if not os.path.exists(img_dir):
                os.makedirs(img_dir)
                log.info(f"创建截图目录：{img_dir}")
            sleep(1)
            self.driver.save_screenshot(img_file)
            log.info(f"截图成功：{img_file}")
            return img_file
        except Exception as e:
            log.error(f"截图失败：{e}")
            return None
