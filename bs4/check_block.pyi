"""
This type stub file was generated by pyright.
"""

import requests

from bs4 import _s

data = requests.get("https://www.crummy.com/").content
data = [x for x in _s(data).block_text()]
