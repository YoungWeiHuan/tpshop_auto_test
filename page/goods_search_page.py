import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class GoodsSearchPage(BaseAction):
    # 加入购物车 按钮
    add_to_cart_btn = By.CSS_SELECTOR, 'body > div.shop-list-tour.ma-to-20.p > div > div.stsho.fr > div.shop-list-splb.p > ul > li > div > div.J_btn_statu > div.p-btn > a'

    @allure.step(title='点击 “加入购物车” 按钮')
    def click_add_to_cart_btn(self):
        self.click(self.add_to_cart_btn)
