from personal_web_driver.driver import Driver
from personal_web_driver.getters.td import TdGetter
from personal_web_driver.getters.th import ThGetter


if __name__ == "__main__":
    driver = Driver(headless_option=True)

    driver.launch("https://www.calendriergratuit.fr/fetes-civiles.html")

    elt = driver.get_element_by_xpath(
        getter=ThGetter,
        method="contains",
        attribute="text",
        value="Saint-Valentin")
