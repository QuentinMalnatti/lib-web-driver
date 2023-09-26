from abc import ABC, abstractmethod

from personal_web_driver.driver import Driver


class AbstractNotifier(ABC):
    URL = None

    @classmethod
    def open(cls, driver: Driver):
        driver.open_tab(url=cls.URL)

    @classmethod
    def close(cls, driver: Driver):
        driver.close_tab()

    @abstractmethod
    def send(self, driver: Driver, receiver: str, message: str = "TEST"):
        raise NotImplementedError
