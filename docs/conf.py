# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

project = 'dummy-module'
release = version = '0.1.0'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
exclude_patterns = ['build']
default_role = 'literal'
napoleon_custom_sections = ['T']
