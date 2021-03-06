import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LoginPage(BaseAction):
    # 用户名 输入框
    login_username = By.ID, 'username'
    # 密码 输入框
    login_password = By.ID, 'password'
    # 验证码 输入框
    login_verify_code = By.ID, 'verify_code'
    # 登录 按钮
    login_btn = By.NAME, 'sbtbutton'

    @allure.step(title='输入用户名')
    def input_username(self, username):
        self.input(self.login_username, username)

    @allure.step(title='输入密码')
    def input_password(self, password):
        self.input(self.login_password, password)

    @allure.step(title='输入验证码')
    def input_verify_code(self, code):
        self.input(self.login_verify_code, code)

    @allure.step(title='点击 “登录” 按钮')
    def click_login_btn(self):
        self.click(self.login_btn)
