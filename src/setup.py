#!/usr/bin/env python

from setuptools import setup, find_packages

requires = [
    'twisted'
]

setup(
    name="Livewire LED Wall",
    description="Websocket Server that will run the led wall",
    author="Team LiveWire",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
