from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='plot',
    version="0.6.5",
    description="A matplotlib frontend executable "
                "using JSON file as user input",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/yuhangwang/plot",
    author="Yuhang(Steven) Wang",
    license="MIT/X11",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
            'console_scripts': [
                    'plot = plot.main:main'
                ],
        },
    python_requires=">3.3",
    install_requires=[
            "matplotlib",
            "typing",
            "numpy",
            "scipy",
            "pyyaml",
        ],
    )
