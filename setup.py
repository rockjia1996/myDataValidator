from setuptools import find_packages, setup

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pythong_data_validator",
    packages=find_packages(include=['python_data_validator']),
    version="0.1.0",
    description="Python Data Validator",
    long_description=long_description,
    url="https://github.com/rockjia1996/python-data-validator",
    author="Yu Jia",
    author_email="rockjia1996@gmail.com",
    license="GNU General Public License v3.0",
    install_requires=[]
)