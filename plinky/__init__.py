# Copyright Amethyst Reese
# Licensed under the MIT license

"""
Dynamic link site>
"""

__author__ = "Amethyst Reese"
from .__version__ import __version__

from .cli import main
from .config import load_config
from .render import render_site
from .types import Config, Link, Page
