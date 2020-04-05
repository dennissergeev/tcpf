#!/usr/bin/env python
# -*- encoding: utf-8
from pathlib import Path
from setuptools import setup, find_packages


executable = Path.cwd().parent / "bin" / "model.x"


setup(
    name="tcpf",
    version="0.1",
    scripts=[executable],
    install_requires=["sh", "jinja2", "f90nml", "numpy", "pandas", "xarray"],
    # metadata to display on PyPI
    author="Denis Sergeev",
    description="This is an Example Package",
    keywords="hello world example examples",
    classifiers=["License :: OSI Approved :: Python Software Foundation License"],
)
