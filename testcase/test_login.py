import allure
import pytest
from selenium.webdriver.common.by import By

from settings import ENV
from testcase.conftest import open_page
from po.event import Event


class TestLogin:
    @pytest.mark.parametrize('username, password, result', [
        (ENV.username, ENV.password, '退出登录'),
        (ENV.username, '1234567', '注册'),
        ("12345678901", ENV.password, "注册"),
    ],ids=('test_login_001','test_login_002','test_login_003'))
    @allure.story('登录')
    def test_login(self, username, password,result,open_page):
        driver = open_page
        Event.event_login(driver, username, password)

        if '退出登录' in result:
            driver.sel_click((By.XPATH,"//div[@class='tabbar']//div[4]"))
            text = driver.sel_get_text((By.XPATH,"//span[contains(text(),'退出登录')]"))
            driver.sel_click((By.XPATH,"//span[contains(text(),'退出登录')]"))
            driver.get(ENV.url)
            assert text == result
        elif '注' in result:
            text = driver.sel_get_text((By.XPATH,'//*[@id="app"]/div/form/div[3]/button[2]'))
            driver.get(ENV.url)
            assert text == result
        elif '注' in result:
            text = driver.sel_get_text((By.XPATH,'//*[@id="app"]/div/form/div[3]/button[2]'))
            assert text == result







