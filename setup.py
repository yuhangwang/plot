from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='plot',
    version="0.6.4",
    description="A matplotlib frontend executable "
                "using JSON file as user input",
    long_description=long_description,
    url="https://github.com/yuhangwang/plot",
    author="Yuhang(Steven) Wang",
    license="MIT/X11",
    packages=find_packages(),
    entry_points={
            'console_scripts': [
                    'plot = plot.main:main'
                ],
        },
    install_requires=[
            "matplotlib",
            "typing",
            "numpy",
            "scipy",
            "pyyaml",
        ],
    )
