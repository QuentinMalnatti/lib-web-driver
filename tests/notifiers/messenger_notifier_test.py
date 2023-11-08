import os

from tests.notifiers.abstract_notifier_test import AbstractNotifierTest
from personal_web_driver.notifiers.messenger_notifier import MessengerNotifier


class MessengerNotifierTest(AbstractNotifierTest):
    RECEIVER = os.getenv("RECEIVER")

    def __init__(self):
        super().__init__(notifier=MessengerNotifier)

    def run(self):
        self._standard_run()


if __name__ == "__main__":
    notifier_test = MessengerNotifierTest()
    notifier_test.run()
