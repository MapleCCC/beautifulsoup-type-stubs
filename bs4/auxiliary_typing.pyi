from typing import Union, Optional, List, Pattern, Callable, Literal, AnyStr
from .element import Tag

Filter = Union[AnyStr, List[AnyStr], Pattern, Callable[[Tag], bool], Literal[True]]
