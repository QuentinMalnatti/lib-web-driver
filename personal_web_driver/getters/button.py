from .abstract_getter import AbstractGetter


class ButtonGetter(AbstractGetter):

    @staticmethod
    def get_xpath(method: str, attribute: str, value: str) -> str:
        xpath = f"//button[{method}"
        if method == "contains" and attribute == "text":
            return xpath + f"(., '{value}')]"
