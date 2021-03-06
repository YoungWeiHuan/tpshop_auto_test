import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class IndexPage(BaseAction):
    # 登录链接 按钮
    login_link_btn = By.CLASS_NAME, 'red'
    # 我的订单 链接
    my_order_link_btn = By.CSS_SELECTOR, 'body > div.tpshop-tm-hander > div.top-hander.clearfix > div > ul > li:nth-child(1) > a'
    # 搜索框
    search_input = By.ID, 'q'
    # 搜索 按钮
    search_btn = By.CLASS_NAME, 'ecsc-search-button'
    # 我的购物车 链接
    my_cart_btn = By.CSS_SELECTOR, '#hd-my-cart > a > div > span'

    @allure.step(title='点击 “登录” 链接')
    def click_login_link(self):
        self.click(self.login_link_btn)

    @allure.step(title='点击 “我的订单” 链接')
    def click_my_order_link(self):
        self.click(self.my_order_link_btn)

    @allure.step(title='输入搜索关键字')
    def input_search(self, keyword):
        allure.attach(keyword, '输入的关键字', allure.attachment_type.TEXT)
        self.input(self.search_input, keyword)
        allure.attach(self.driver.get_screenshot_as_png(), '输入关键字截图', allure.attachment_type.PNG)

    @allure.step(title='点击 “搜索” 按钮')
    def click_search_btn(self):
        self.click(self.search_btn)

    @allure.step(title='点击 “我的购物车” 按钮')
    def click_my_cart_btn(self):
        self.click(self.my_cart_btn)
