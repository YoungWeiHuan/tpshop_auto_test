import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class GoodsDetailPage(BaseAction):
    # 加入购物车 按钮
    add_to_cart_btn = By.ID, 'join_cart'
    # iframe
    cart_iframe = By.CSS_SELECTOR, '[id*="layui-layer-iframe"]'
    # 添加成功
    result = By.CSS_SELECTOR, '.conect-title span'

    @allure.step(title='点击 “加入购物车” 按钮')
    def click_add_to_cart_btn(self):
        self.click(self.add_to_cart_btn)

    @allure.step(title='获取 “添加成功” 文本信息')
    def get_result(self):
        self.switch_to(self.cart_iframe)
        return self.find_el(self.result).text
