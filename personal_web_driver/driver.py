from time import sleep
from typing import Type, Any, Optional
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager

from personal_logger.logger import LoggerDecorator, LoggerBase

from .getters.abstract_getter import AbstractGetter


class Driver(object):

    def __init__(self, headless_option: bool = False, lang: str = "fr", experimental_options: Optional[list[dict[str, Any]]] = None):
        options = uc.ChromeOptions()
        options.add_argument(f"--lang={lang}")

        if experimental_options:
            for o in experimental_options:
                options.add_experimental_option("prefs", o)

        path_driver = ChromeDriverManager().install().replace("THIRD_PARTY_NOTICES.chromedriver", "chromedriver")
        self.__driver = uc.Chrome(driver_executable_path=path_driver, options=options, headless=headless_option)

    @LoggerDecorator.log(stage="Launch driver")
    def launch(self, url: str):
        self.__driver.get(url=url)

    @LoggerDecorator.log(stage="Quit driver")
    def quit(self):
        self.__driver.quit()

    @LoggerDecorator.log(stage="Refresh driver")
    def refresh(self):
        self.__driver.refresh()

    @LoggerDecorator.log(stage="Save a screenshot")
    def save_screenshot(self, path_screenshot):
        self.__driver.save_screenshot(path_screenshot)

    @LoggerDecorator.log(stage="get page source")
    def get_page_source(self):
        return self.__driver.page_source

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

    def get_element_by_id(self, value: str):
        return self.__driver.find_element(By.ID, value)

    def get_element_by_tag_name(self, value: str):
        return self.__driver.find_element(By.TAG_NAME, value)

    @classmethod
    def fill_input(cls, element, value: str):
        element.send_keys(value)

    def click(self, element, sleep_time=1):
        action = ActionChains(self.__driver)
        action.move_to_element(element).click().perform()
        sleep(sleep_time)

    def open_tab(self, url: str):
        self.__driver.switch_to.new_window('tab')
        self.__driver.get(url=url)

    def switch_tab(self, index: int):
        self.__driver.switch_to.window(self.__driver.window_handles[index])

    def close_tab(self):
        self.__driver.close()

    @staticmethod
    @LoggerDecorator.log(stage="Add some human behavior by running a pause")
    def sleep_rand(lower: int, upper: int):
        LoggerBase.print_timed_message(msg=f"Sleep time range : {lower} and {upper} seconds")
        sleep_time = randint(lower, upper)
        LoggerBase.print_timed_message(msg=f"Pause run for {sleep_time} seconds")
        sleep(sleep_time)

    @staticmethod
    @LoggerDecorator.log(stage="Freeze")
    def freeze():
        while True:
            pass
