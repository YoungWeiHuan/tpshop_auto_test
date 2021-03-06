import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class OrderPayPage(BaseAction):
    # 订单状态信息
    tips_info = By.CSS_SELECTOR, '.erhuh h3'
    # 货到付款 选框
    arrived_pay = By.CSS_SELECTOR, '#cart4_form > div > div > dl > dd > div > div.po-re.dsfzf-ee > ul > li:nth-child(2) > div > label > img'
    # 确认支付方式 按钮
    pay_btn = By.CLASS_NAME, 'button-style-5'

    @allure.step(title='获取订单状态信息')
    def get_tips_info(self):
        return self.find_el(self.tips_info).text

    @allure.step(title='点击 “货到付款” 选框')
    def click_arrived_pay(self):
        self.click(self.arrived_pay)

    @allure.step(title='点击 “确认支付方式” 按钮')
    def click_pay_btn(self):
        self.click(self.pay_btn)
