#!/usr/bin/env python
# -*- encoding: utf-8
"""Core module."""
from pathlib import Path
import subprocess as sb


__all__ = ("Model",)


class Model:
    """Dummy model class."""

    def __init__(self):
        self.name = "dummy_model"

    def compile(self):
        cmpl_scr = Path.cwd().parent / "src" / "compile.sh"
        print(cmpl_scr)
        sb.call(cmpl_scr, shell=True)
