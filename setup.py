# -*- coding: utf-8 -*-
from numpy import get_include as numpy_get_include
from setuptools import setup


setup(
    name="dummm",
    version='0.0.1',
    packages='dummm',
    include_dirs=[numpy_get_include()],
)
