from .abstract_getter import AbstractGetter


class DivGetter(AbstractGetter):

    @staticmethod
    def get_xpath(method: str, attribute: str, value: str) -> str:
        xpath = "//div["
        if method == "contains":
            xpath += f"{method}("
            if attribute == "aria-label":
                xpath += f"@{attribute}"
            else:
                xpath += f"{attribute}()"
            return xpath + f", '{value}')]"
