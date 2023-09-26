from .abstract_getter import AbstractGetter


class TdGetter(AbstractGetter):

    @staticmethod
    def get_xpath(method: str, attribute: str, value: str) -> str:
        xpath = f"//td[{method}"
        if method == "contains" and attribute == "text":
            return xpath + f"(., '{value}')]"
