import pytest
from common.log import log
from po.event import Event
from po.home_page import HomePage
from settings import ENV


@pytest.fixture(scope="class")
def login():
    global driver
    driver = HomePage()
    Event().event_login(driver, ENV.username, ENV.password)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def open_page():
    global driver
    driver = HomePage()
    driver.get(ENV.url)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    out = yield
    result = out.get_result()
    log.info(f"Test result: {result}")
    log.info(f"execution time: {round(call.duration, 2)} second")
    if result.failed:
        try:
            log.info('error.screenshot.')
            driver.allure_save_screenshot('error.screenshot')
        except Exception as e:
            log.error(f"Error while taking screenshot: {e}")
            pass
