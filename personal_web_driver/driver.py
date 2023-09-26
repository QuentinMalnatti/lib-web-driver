from typing import Type

from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager

from .getters.abstract_getter import AbstractGetter


class Driver(object):

    def __init__(self):
        options = uc.ChromeOptions()
        self.__driver = uc.Chrome(driver_executable_path=ChromeDriverManager().install(), options=options)

    def launch(self, url: str):
        self.__driver.get(url=url)

    def quit(self):
        self.__driver.quit()

    def refresh(self):
        self.__driver.refresh()

    def get_element_by_xpath(self, getter: Type[AbstractGetter], method: str, attribute: str, value: str):
        xpath = getter.get_xpath(method=method, attribute=attribute, value=value)
        return self.__driver.find_element(By.XPATH, xpath)

    @classmethod
    def get_parent_element(cls, element, level=1):
        for i in range(0, level):
            element = element.find_element(By.XPATH, "..")
        return element

    def get_element_by_class_name(self, value: str):
        return self.__driver.find_element(By.CLASS_NAME, value)

    def get_element_by_tag_name(self, value: str):
        return self.__driver.find_element(By.TAG_NAME, value)

    @classmethod
    def fill_input(cls, element, value: str):
        element.send_keys(value)

    @classmethod
    def click(cls, element):
        element.click()

    def open_tab(self, url: str):
        self.__driver.switch_to.new_window('tab')
        self.__driver.get(url=url)

    def switch_tab(self, index: int):
        self.__driver.switch_to.window(self.__driver.window_handles[index])

    def close_tab(self):
        self.__driver.close()
