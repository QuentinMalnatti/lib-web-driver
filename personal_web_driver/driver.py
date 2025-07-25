from time import sleep
from typing import Type, Any, Optional
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager

from .logger import LoggerDecoratorWebDriver
from .getters.abstract_getter import AbstractGetter


class Driver(object):

    def __init__(self,
                 headless_option: bool = False,
                 driver_options: Optional[list[str]] = None,
                 experimental_options: Optional[list[dict[str, Any]]] = None):

        options = uc.ChromeOptions()

        if driver_options:
            for do in driver_options:
                options.add_argument(do)

        if experimental_options:
            for eo in experimental_options:
                options.add_experimental_option("prefs", eo)

        path_driver = ChromeDriverManager().install().replace("THIRD_PARTY_NOTICES.chromedriver", "chromedriver")
        self.__driver = uc.Chrome(driver_executable_path=path_driver, options=options, headless=headless_option)

        self.__current_page_source = None

    def get_current_page_source(self):
        return self.__current_page_source

    def set_current_page_source(self):
        self.__current_page_source = self.__driver.page_source

    @LoggerDecoratorWebDriver.log(stage="Launch driver")
    def launch(self, url: str):
        self.__driver.get(url=url)
        self.set_current_page_source()

    @LoggerDecoratorWebDriver.log(stage="Quit driver")
    def quit(self):
        self.__driver.quit()

    @LoggerDecoratorWebDriver.log(stage="Refresh driver")
    def refresh(self):
        self.__driver.refresh()
        self.set_current_page_source()

    @LoggerDecoratorWebDriver.log(stage="Save a screenshot")
    def save_screenshot(self, path_screenshot):
        self.__driver.save_screenshot(path_screenshot)

    def get_element_by_xpath(self, getter: Type[AbstractGetter], method: str, attribute: str, value: str, multiple=False):
        xpath = getter.get_xpath(method=method, attribute=attribute, value=value)

        if multiple:
            return self.__driver.find_elements(By.XPATH, xpath)

        return self.__driver.find_element(By.XPATH, xpath)

    @classmethod
    def get_parent_element(cls, element, level=1):
        for i in range(0, level):
            element = element.find_element(By.XPATH, "..")
        return element

    def get_element_by_class_name(self, value: str, multiple=False):
        if multiple:
            return self.__driver.find_elements(By.CLASS_NAME, value)

        return self.__driver.find_element(By.CLASS_NAME, value)

    def get_element_by_id(self, value: str, multiple=False):
        if multiple:
            return self.__driver.find_elements(By.ID, value)

        return self.__driver.find_element(By.ID, value)

    def get_element_by_name(self, value: str, multiple=False):
        if multiple:
            return self.__driver.find_elements(By.NAME, value)

        return self.__driver.find_element(By.NAME, value)

    def get_element_by_tag_name(self, value: str, multiple=False):
        if multiple:
            return self.__driver.find_elements(By.TAG_NAME, value)

        return self.__driver.find_element(By.TAG_NAME, value)

    @classmethod
    def fill_input(cls, element, value: str):
        element.send_keys(value)

    def click(self, element, sleep_time=1):
        action = ActionChains(self.__driver)
        action.move_to_element(element).click().perform()
        sleep(sleep_time)
        self.set_current_page_source()

    def open_tab(self, url: str):
        self.__driver.switch_to.new_window('tab')
        self.__driver.get(url=url)
        self.set_current_page_source()

    def switch_tab(self, index: int):
        self.__driver.switch_to.window(self.__driver.window_handles[index])
        self.set_current_page_source()

    def close_tab(self):
        self.__driver.close()
        self.set_current_page_source()

    @staticmethod
    def sleep_rand(lower: int, upper: int):
        sleep_time = randint(lower, upper)
        LoggerDecoratorWebDriver.get_logger_base().print_timed_message(msg=f"Add some human behavior by running a pause between {lower} and {upper} seconds ({sleep_time} seconds applied)")
        sleep(sleep_time)

    @staticmethod
    @LoggerDecoratorWebDriver.log(stage="Freeze")
    def freeze():
        while True:
            pass

