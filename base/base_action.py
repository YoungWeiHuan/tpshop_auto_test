class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_el(self, feature):
        return self.driver.find_element(*feature)

    def find_els(self, feature):
        return self.driver.find_elements(*feature)

    def click(self, feature):
        return self.find_el(feature).click()

    def input(self, feature, content):
        return self.find_el(feature).send_keys(content)

    def clear(self, feature):
        return self.find_el(feature).clear()

    def switch_to(self, frame_feature):
        return self.driver.switch_to.frame(self.find_el(frame_feature))

    def switch_to_default(self):
        return self.driver.switch_to.default_content()

    def switch_window(self):
        handlers = self.driver.window_handles
        return self.driver.switch_to.window(handlers[-1])