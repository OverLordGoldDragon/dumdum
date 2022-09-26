# -*- coding: utf-8 -*-
from numpy import get_include as numpy_get_include
from setuptools import setup
import dummm

setup(
    name="dummm",
    version=dummm.__version__,
    packages=['dummm'],
    include_dirs=[numpy_get_include()],
    install_requires=["numpy>=1.20.0"],
)
