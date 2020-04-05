#!/usr/bin/env python
# -*- encoding: utf-8
from pathlib import Path
from setuptools import setup, find_packages

# from setuptools.command.build_py import build_py


script_dir = Path.cwd() / "bin"
scripts = [str(i) for i in [script_dir / "run_model.py"]]
print(scripts)


setup(
    name="tcpf",
    version="0.1",
    package_dir={"tcpf": "python/tcpf"},
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    scripts=scripts,
    install_requires=["sh", "jinja2", "f90nml", "numpy", "pandas", "xarray"],
    # metadata to display on PyPI
    author="Denis Sergeev",
    description="This is an Example Package",
    keywords="hello world example examples",
    classifiers=["License :: OSI Approved :: Python Software Foundation License"],
)
