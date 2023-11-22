from setuptools import setup

setup(
    name="PersonalWebDriver",
    url="https://github.com/QuentinMalnatti/lib-driver",
    author="Quentin Malnatti",
    packages=["personal_web_driver", "personal_web_driver.getters", "personal_web_driver.notifiers"],
    install_requires=["personal_logger", "selenium", "undetected_chromedriver", "webdriver_manager"],
    version="1.0.0",
    description="Personal web driver",
    long_description=open("README.md").read(),
)
