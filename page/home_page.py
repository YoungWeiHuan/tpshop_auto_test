import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class HomePage(BaseAction):
    # 待付款 链接
    to_be_pay_link = By.CLASS_NAME, 'selected'
    # 立即付款 按钮
    pay_btn = By.CLASS_NAME, 'ps_lj'

    @allure.step(title='点击 “待付款” 链接')
    def click_to_be_pay_link(self):
        self.click(self.to_be_pay_link)

    @allure.step(title='点击 “立即付款” 按钮')
    def click_pay_btn(self):
        self.click(self.pay_btn)
