import logging
import time
import allure
from page.cart_page import CartPage
from page.home_page import HomePage
from page.index_page import IndexPage
from page.order_page import OrderPage
from page.order_pay_page import OrderPayPage
from utils.driver_utils import DriverUtils


@allure.feature('订单模块')
class TestOrder:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        self.index_page = IndexPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.order_page = OrderPage(self.driver)
        self.order_pay_page = OrderPayPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.driver.get('http://localhost/')

    def teardown(self):
        time.sleep(2)
        DriverUtils.quit_driver()

    def teardown_class(self):
        DriverUtils.set_driver_select(False)
        DriverUtils.get_driver().get_screenshot_as_file('./screenshot/tpshop.png')
        DriverUtils.quit_driver()

    @allure.story('购物车结算，订单提交成功')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_submit_order(self):
        self.index_page.click_my_cart_btn()
        self.cart_page.click_go_to_pay_btn()
        time.sleep(6)
        logging.info('wait 6s for page display')
        self.order_page.click_submit_order_btn()
        assert '订单提交成功，请您尽快付款！' == self.order_pay_page.get_tips_info()

    @allure.story('选择货到付款，支付成功')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_pay(self):
        self.index_page.click_my_order_link()
        self.index_page.switch_window()
        logging.info('switch to other window')
        self.home_page.click_to_be_pay_link()
        self.home_page.click_pay_btn()
        self.home_page.switch_window()
        logging.info('switch to other window')
        self.order_pay_page.click_arrived_pay()
        self.order_pay_page.click_pay_btn()
        time.sleep(3)
        logging.info('wait 3s for page display')
        assert '订单提交成功，我们将在第一时间给你发货！' == self.order_pay_page.get_tips_info()
