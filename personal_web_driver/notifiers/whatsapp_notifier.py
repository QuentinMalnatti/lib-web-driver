from time import sleep

from selenium.common.exceptions import NoSuchElementException

from .abstract_notifier import AbstractNotifier
from personal_web_driver.driver import Driver
from personal_web_driver.getters.span import SpanGetter
from personal_logger.logger import LoggerDecorator


class WhatsappNotifier(AbstractNotifier):
    URL = "https://web.whatsapp.com/"

    @LoggerDecorator.log_success_as_success(
        stage="Send Whatsapp message",
        exception_to_catch=NoSuchElementException,
        error_msg=f"Impossible to send the message",
        to_raise=True,
    )
    def send(self, driver: Driver, receiver: str, message: str = "TEST"):
        user = driver.get_element_by_xpath(getter=SpanGetter, method="contains", attribute="title", value=receiver)
        driver.click(element=user)

        text_box = driver.get_element_by_class_name(value="_3Uu1_")
        driver.fill_input(element=text_box, value=message)

        send_button = driver.get_element_by_class_name(value="epia9gcq")
        driver.click(element=send_button)

        sleep(1)
