# setup.py
from setuptools import setup, find_packages

setup(
    name="libreria_selenium_pers",
    version="0.4.1",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "requests",
        "webdriver-manager"
    ],
    author="Matias Arriete",
    description="Una librería de Python para uso personal",
)
