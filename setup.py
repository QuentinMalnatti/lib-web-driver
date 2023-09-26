from setuptools import setup

setup(
    name='PersonalWebDriver',
    url='https://github.com/QuentinMalnatti/lib-driver',
    author='Quentin Malnatti',
    packages=['personal_web_driver'],
    install_requires=['personal_logger'],
    version='0.1.1',
    description='Personal web driver',
    long_description=open('README.md').read(),
)