from setuptools import find_packages, setup

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="myDataValidator",
    version="0.1.0",
    packages=find_packages(),
    description="Python Data Validator",
    long_description=long_description,
    url="https://github.com/rockjia1996/myDataValidator",
    author="Yu Jia",
    author_email="rockjia1996@gmail.com",
    license="GNU General Public License v3.0",
)