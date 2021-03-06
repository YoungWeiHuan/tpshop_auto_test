import logging
import time
import allure
from page.goods_detail_page import GoodsDetailPage
from page.goods_search_page import GoodsSearchPage
from page.index_page import IndexPage
from utils.driver_utils import DriverUtils


@allure.feature('购物车模块')
class TestCart:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        self.index_page = IndexPage(self.driver)
        self.goods_search_page = GoodsSearchPage(self.driver)
        self.goods_detail_page = GoodsDetailPage(self.driver)
        self.driver.get('http://localhost/')

    def teardown(self):
        time.sleep(2)
        DriverUtils.quit_driver()

    @allure.story('搜索小米手机5，添加购物车成功')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart(self):
        self.index_page.input_search('小米手机5')
        logging.info('search with 小米手机5')
        self.index_page.click_search_btn()
        self.goods_search_page.click_add_to_cart_btn()
        self.goods_detail_page.click_add_to_cart_btn()
        time.sleep(3)
        logging.info('wait 3s for page display')
        assert '添加成功' == self.goods_detail_page.get_result()
