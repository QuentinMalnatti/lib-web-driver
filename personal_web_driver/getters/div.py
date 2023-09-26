from .abstract_getter import AbstractGetter


class DivGetter(AbstractGetter):

    @staticmethod
    def get_xpath(method: str, attribute: str, value: str) -> str:
        return f"//div[{method}({attribute}(), '{value}')]"
