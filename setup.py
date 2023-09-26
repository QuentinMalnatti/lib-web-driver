from setuptools import setup

setup(
    name="PersonalWebDriver",
    url="https://github.com/QuentinMalnatti/lib-driver",
    author="Quentin Malnatti",
    packages=["personal_web_driver", "personal_web_driver.getters", "personal_web_driver.notifiers"],
    install_requires=["personal_logger"],
    version="0.1.2",
    description="Personal web driver",
    long_description=open("README.md").read(),
)
