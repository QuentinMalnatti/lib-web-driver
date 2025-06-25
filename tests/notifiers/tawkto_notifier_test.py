from tests.notifiers.abstract_notifier_test import AbstractNotifierTest
from personal_web_driver.notifiers.tawkto_notifier import TawkToNotifier


class TawkToNotifierTest(AbstractNotifierTest):

    def __init__(self, headless_option: bool = False):
        super().__init__(notifier=TawkToNotifier, headless_option=headless_option)

    def run(self):
        self._standard_run()


if __name__ == "__main__":
    notifier_test = TawkToNotifierTest(headless_option=False)
    notifier_test.run()
