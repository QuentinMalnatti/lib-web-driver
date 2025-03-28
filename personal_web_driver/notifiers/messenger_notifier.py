import os

from selenium.common.exceptions import NoSuchElementException

from .abstract_notifier import AbstractNotifier
from personal_web_driver.driver import Driver
from personal_web_driver.getters.button import ButtonGetter
from personal_web_driver.getters.span import SpanGetter
from personal_web_driver.getters.div import DivGetter
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
        self.__close_cookies_popup_if_exists(driver=driver)

        input_id = driver.get_element_by_id(value="email")
        driver.fill_input(element=input_id, value=os.getenv("ID"))
        driver.sleep_rand(2, 5)

        input_pwd = driver.get_element_by_id(value="pass")
        driver.fill_input(element=input_pwd, value=os.getenv("PWD"))
        driver.sleep_rand(2, 5)

        button_login = driver.get_element_by_id(value="loginbutton")
        driver.click(element=button_login, sleep_time=10)

        driver.sleep_rand(2, 3)
        self.__close_restore_old_messages_pop_up_if_exists(driver)

    @staticmethod
    @LoggerDecorator.log_success_as_success(
        stage="Close cookies pop-up",
        exception_to_catch=NoSuchElementException,
        error_msg="No cookies pop-up to handle",
        to_raise=False
    )
    def __close_cookies_popup_if_exists(driver: Driver):
        button_cookies = driver.get_element_by_xpath(
            getter=ButtonGetter, method="contains", attribute="text", value="Refuser les cookies"
        )
        driver.click(button_cookies, sleep_time=2)

    @staticmethod
    @LoggerDecorator.log_success_as_success(
        stage="Close restore old messages pop-up",
        exception_to_catch=NoSuchElementException,
        error_msg="No restore old messages pop-up to handle",
        to_raise=False
    )
    def __close_restore_old_messages_pop_up_if_exists(driver: Driver):
        # test if pop-up exists
        driver.get_element_by_id(value="mw-numeric-code-input-prevent-composer-focus-steal")

        button_close_pin_pop_up = driver.get_element_by_xpath(
            getter=DivGetter, method="contains", attribute="aria-label", value="Fermer"
        )
        driver.click(button_close_pin_pop_up, sleep_time=2)

        button_do_not_restore = driver.get_element_by_xpath(
            getter=DivGetter, method="contains", attribute="aria-label", value="Ne pas restaurer les messages"
        )
        driver.click(button_do_not_restore, sleep_time=2)

    @LoggerDecorator.log_success_as_success(
        stage="Send Messenger message",
        exception_to_catch=NoSuchElementException,
        error_msg="Impossible to send the message",
        to_raise=True,
    )
    def send(self, driver: Driver, receiver: str, message: str = "TEST"):
        try:
            user = self.get_user(driver=driver, receiver=receiver)
        except NoSuchElementException:
            user = self.get_user(driver=driver, receiver=f"{receiver} ")

        driver.click(element=user)

        message_input = driver.get_element_by_xpath(getter=DivGetter, method="contains", attribute="aria-label", value="Écrire un message")
        driver.fill_input(element=message_input, value=message)

        send_button = driver.get_element_by_xpath(getter=DivGetter, method="contains", attribute="aria-label", value="Appuyer sur Entrée pour envoyer")
        driver.click(element=send_button)

    @staticmethod
    def get_user(driver: Driver, receiver: str):
        return driver.get_element_by_xpath(getter=SpanGetter, method="equals", attribute="text", value=receiver)
