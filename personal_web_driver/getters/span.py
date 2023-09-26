from .abstract_getter import AbstractGetter


class SpanGetter(AbstractGetter):

    @staticmethod
    def get_xpath(method: str, attribute: str, value: str) -> str:
        xpath = f"//span[{method}"
        if attribute == "title":
            return xpath + f"(@{attribute}, '{value}')]"
