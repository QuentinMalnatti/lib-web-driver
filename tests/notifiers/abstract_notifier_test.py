import os
from typing import Type
from abc import ABC, abstractmethod

from personal_web_driver.notifiers.abstract_notifier import AbstractNotifier
from personal_web_driver.driver import Driver


class AbstractNotifierTest(ABC):
    RECEIVER = os.getenv("RECEIVER")
    MESSAGE = "Test message"

    def __init__(self, notifier: Type[AbstractNotifier], headless_option: bool = False):
        self._notifier = notifier()
        self._driver = Driver(headless_option=headless_option)
        self._driver.launch(url=self._notifier.URL)

    def _standard_run(self):
        self._notifier.connect(driver=self._driver)
        self._notifier.send(driver=self._driver, receiver=self.RECEIVER, message=self.MESSAGE)

    @abstractmethod
    def run(self):
        raise NotImplementedError
