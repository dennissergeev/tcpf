#!/usr/bin/env python
# -*- encoding: utf-8
from setuptools import setup, find_packages

# from setuptools.command.build_py import build_py


scripts = ["bin/run_model.py"]


setup(
    name="tcpf",
    version="0.1",
    packages=find_packages("src/python"),
    package_dir={"tcpf": "src/python/tcpf"},
    include_package_data=True,
    zip_safe=False,
    scripts=scripts,
    install_requires=["sh", "jinja2", "f90nml", "numpy", "pandas", "xarray"],
    # metadata to display on PyPI
    author="Denis Sergeev",
    description="This is an Example Package",
    keywords="hello world example examples",
    classifiers=["License :: OSI Approved :: Python Software Foundation License"],
)
