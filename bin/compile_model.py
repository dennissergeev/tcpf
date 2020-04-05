#!/usr/bin/env python
# -*- encoding: utf-8
from pathlib import Path

from tcpf import Model


m = Model(Path("."))
m.compile()
