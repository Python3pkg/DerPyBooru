# -*- coding: utf-8 -*-

"""
Derpibooru API bindings
~~~~~~~~~~~~~~~~~~~~~~~

Python bindings for Derpibooru's API

Typical usage:

>>> from derpibooru import Search, sort
>>> for image in Search().sort_by(sort.score):
...   print(image.url)

Full API Documentation is found at <https://derpiboo.ru/api>.

Library documentation is found at <https://github.com/joshua-stone/DerPyBooru>.

"""

__title__ = "DerPyBooru"
__version__ = "0.3"
__author__ = "Joshua Stone"
__license__ = "Simplified BSD Licence"
__copyright__ = "Copyright (c) 2014, Joshua Stone"

from .search import Search
from .query import query
from . import sort

__all__ = [
  "Search",
  "sort.random",
  "sort.score",
  "sort.relevance",
  "sort.width",
  "sort.height",
  "sort.comments",
  "sort.random",
  "sort.sorting_methods"
]
