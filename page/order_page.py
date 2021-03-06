import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class OrderPage(BaseAction):
    # 提交订单 按钮
    submit_order_btn = By.CLASS_NAME, 'Sub-orders'

    @allure.step(title='点击 “提交订单” 按钮')
    def click_submit_order_btn(self):
        self.click(self.submit_order_btn)