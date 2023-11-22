from .abstract_getter import AbstractGetter


class SpanGetter(AbstractGetter):

    @staticmethod
    def get_xpath(method: str, attribute: str, value: str) -> str:
        xpath = "//span["
        if method == "contains":
            xpath += f"{method}"
            if attribute == "title":
                return xpath + f"(@{attribute}, '{value}')]"
        if method == "equals":
            if attribute == "text":
                return xpath + f"text() = '{value}']"
