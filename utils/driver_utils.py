import logging

from selenium import webdriver


class DriverUtils:
    __driver = None
    __driver_select = False

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            logging.info('create chrome driver')
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)
        else:
            logging.info('use existed chrome driver')
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None and cls.__driver_select == False:
            logging.info('quit chrome driver')
            cls.__driver.quit()
            cls.__driver = None
        else:
            logging.info('chrome driver is still alive')

    @classmethod
    def set_driver_select(cls, select):
        cls.__driver_select = select
