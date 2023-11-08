import os

from selenium.common.exceptions import NoSuchElementException

from .abstract_notifier import AbstractNotifier
from personal_web_driver.driver import Driver
from personal_web_driver.getters.button import ButtonGetter
from personal_web_driver.getters.span import SpanGetter
from personal_logger.logger import LoggerDecorator


class MessengerNotifier(AbstractNotifier):
    URL = "https://www.messenger.com/"

    @LoggerDecorator.log_success_as_success(
        stage="Connect to Messenger",
        exception_to_catch=NoSuchElementException,
        error_msg="Impossible to connect",
        to_raise=True,
    )
    def connect(self, driver: Driver):
        try:
            button_cookies = driver.get_element_by_xpath(
                getter=ButtonGetter, method="contains", attribute="text", value="Refuser les cookies"
            )
            driver.click(button_cookies)
        except NoSuchElementException:
            pass

        input_id = driver.get_element_by_id(value="email")
        driver.fill_input(element=input_id, value=os.getenv("ID"))

        input_pwd = driver.get_element_by_id(value="pass")
        driver.fill_input(element=input_pwd, value=os.getenv("PWD"))

        button_login = driver.get_element_by_id(value="loginbutton")
        driver.click(element=button_login, sleep_time=5)

    @LoggerDecorator.log_success_as_success(
        stage="Send Messenger message",
        exception_to_catch=NoSuchElementException,
        error_msg="Impossible to send the message",
        to_raise=True,
    )
    def send(self, driver: Driver, receiver: str, message: str = "TEST"):
        user = driver.get_element_by_xpath(getter=SpanGetter, method="contains", attribute="title", value=receiver)
        driver.click(element=user)
        while True:
            pass
