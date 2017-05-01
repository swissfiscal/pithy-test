#!/usr/bin/python
# coding=utf-8
from setuptools import setup, find_packages

setup(
    name="pithy",
    version="0.0.6",
    keywords=("interface", "automation", "testing", "pithy"),
    description=u"简化接口测试",
    long_description=u"简化接口测试",
    url="https://github.com/yuyu1987/pithy-test",
    author="coolfish",
    author_email="hgbaczt@gmail.com",
    packages=['pithy'],
    include_package_data=True,
    platforms="any",
    install_requires=['requests', 'sqlalchemy', 'objectpath', 'click',
                      'jinja2', 'pyyaml', 'Appium-Python-Client', 'thriftpy'],
    entry_points='''
    [console_scripts]
    pithy-cli=pithy.cli:cli
    '''
)