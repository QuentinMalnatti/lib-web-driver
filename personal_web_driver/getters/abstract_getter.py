from abc import ABC, abstractmethod


class AbstractGetter(ABC):
    @staticmethod
    @abstractmethod
    def get_xpath(method: str, attribute: str, value: str) -> str:
        raise NotImplementedError
