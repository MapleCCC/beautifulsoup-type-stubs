from typing import Union, Optional, List, Pattern, Callable, Literal, AnyStr, NewType
from .element import Tag

Filter = Union[AnyStr, List[AnyStr], Pattern, Callable[[Tag], bool], Literal[True]]

ResultSetType = NewType("ResultSetType", List[Tag])
