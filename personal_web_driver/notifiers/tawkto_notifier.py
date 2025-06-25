import os

from selenium.common.exceptions import NoSuchElementException

from .abstract_notifier import AbstractNotifier
from personal_web_driver.driver import Driver
from personal_logger.logger import LoggerDecorator


class TawkToNotifier(AbstractNotifier):
    URL = "https://dashboard.tawk.to/login"

    @LoggerDecorator.log_success_as_success(
        stage="Connect to TawkTo",
        exception_to_catch=NoSuchElementException,
        error_msg="Impossible to connect",
        to_raise=True,
    )
    def connect(self, driver: Driver):
        input_id = driver.get_element_by_id(value="email")
        driver.fill_input(element=input_id, value=os.getenv("UID"))
        driver.sleep_rand(2, 5)

        input_pwd = driver.get_element_by_id(value="password")
        driver.fill_input(element=input_pwd, value=os.getenv("UPWD"))
        driver.sleep_rand(2, 5)

        button_sign_in = driver.get_element_by_id(value="submit-login")
        driver.click(element=button_sign_in, sleep_time=10)

    @LoggerDecorator.log_success_as_success(
        stage="Send TawkTo message",
        exception_to_catch=NoSuchElementException,
        error_msg="Impossible to send the message",
        to_raise=True,
    )
    def send(self, driver: Driver, receiver: str, message: str = "TEST"):
        button_inbox = driver.get_element_by_id(value="tawk-inbox-nav")
        driver.click(element=button_inbox, sleep_time=10)

        self.__open_ticket(driver, receiver)

        message_input = driver.get_element_by_class_name(value="tawk-message-input")
        driver.fill_input(element=message_input, value=message)

        send_button = driver.get_element_by_class_name(value="tawk-message-send")
        driver.click(element=send_button)

    @staticmethod
    def __open_ticket(driver: Driver, receiver: str):
        list_items = driver.get_element_by_tag_name(value="p", multiple=True)  # get_element_by_class_name(value="list-item", multiple=True)
        for e in list_items:
            if e.text == receiver:
                driver.click(element=e, sleep_time=5)
                break
