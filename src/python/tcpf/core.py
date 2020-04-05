#!/usr/bin/env python
# -*- encoding: utf-8
"""Core module."""
from pathlib import Path
import sh
import subprocess as sb


__all__ = ("Model",)
thisdir = Path(__file__).parent


class Model:
    """Dummy model class."""

    def __init__(self, topdir):
        self.name = "dummy_model"
        self.topdir = topdir

    def compile(self):
        cmpl_scr = self.topdir / "src" / "fortran" / "compile.sh"
        sb.call(f"./{cmpl_scr.name}", shell=True, cwd=str(cmpl_scr.parent))

    def run(self):
        run_scr = self.topdir / "bin" / "model.x"
        print(run_scr)
        sb.call(str(run_scr), shell=True)
