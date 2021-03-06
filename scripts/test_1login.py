import logging
import time
import allure
import pytest
from base.json_analyze import analyze_data
from page.index_page import IndexPage
from page.login_page import LoginPage
from utils.driver_utils import DriverUtils


@allure.feature('登录模块')
class TestLogin:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_driver_select(True)
        self.index_page = IndexPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.driver.get('http://localhost/')

    def teardown(self):
        time.sleep(2)
        DriverUtils.quit_driver()

    @allure.story('用户密码正确，登录成功')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize('params', analyze_data('login_data.json'))
    def test_login(self, params):
        self.index_page.click_login_link()
        self.login_page.input_username(params['username'])
        self.login_page.input_password(params['password'])
        self.login_page.input_verify_code(params['code'])
        self.login_page.click_login_btn()
        logging.info('login with {}--{}--{}'.format(params['username'], params['password'], params['code']))
        time.sleep(3)
        logging.info('wait 3s for page display')
        assert params['msg'] in self.driver.title

