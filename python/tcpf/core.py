#!/usr/bin/env python
# -*- encoding: utf-8
"""Core module."""
from pathlib import Path
import subprocess as sb


__all__ = ("Model",)
thisdir = Path(__file__).parent


class Model:
    """Dummy model class."""

    def __init__(self):
        self.name = "dummy_model"

    def compile(self):
        cmpl_scr = thisdir.parent.parent / "src" / "compile.sh"
        print(cmpl_scr)
        sb.call(cmpl_scr, shell=True)

    def run(self):
        run_scr = thisdir.parent.parent / "bin" / "model.x"
        print(run_scr)
        sb.call(run_scr, shell=True)
