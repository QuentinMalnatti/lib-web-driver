from tests.notifiers.abstract_notifier_test import AbstractNotifierTest
from personal_web_driver.notifiers.messenger_notifier import MessengerNotifier


class MessengerNotifierTest(AbstractNotifierTest):

    def __init__(self, headless_option: bool = False):
        super().__init__(notifier=MessengerNotifier, headless_option=headless_option)

    def run(self):
        self._standard_run()


if __name__ == "__main__":
    notifier_test = MessengerNotifierTest(headless_option=True)
    notifier_test.run()
