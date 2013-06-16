#!/usr/bin/env python

from setuptools import setup, find_packages

requires = [
    "pyserial",
    "Twisted==12.2.0",
    "autobahn==0.5.9",
    "wsgiref==0.1.2",
]

setup(
    name="Livewire LED Wall",
    description="Websocket Server that will run the led wall",
    author="Team LiveWire",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
