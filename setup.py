# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.4"


REQUIRES = ["connexion"]

with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()
    if not install_requirements:
        print("Unable to read requirements")
        sys.exit(2)

setup(
    name=NAME,
    version=VERSION,
    description="User Management Service",
    author_email="john.doe@example.com",
    url="",
    keywords=["Swagger", "User Management Service"],
    install_requires=install_requirements,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    This is a sample REST user service definition.
    """
)

