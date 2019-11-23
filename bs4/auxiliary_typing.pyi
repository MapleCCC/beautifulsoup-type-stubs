from typing import *

from .element import Tag

try:
    Filter = Union[AnyStr, List[AnyStr], Pattern, Callable[[Tag], bool], Literal[bool]]
except NameError:
    Filter = Union[AnyStr, List[AnyStr], Pattern, Callable[[Tag], bool], bool]