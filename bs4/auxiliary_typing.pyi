from typing import AnyStr, Callable, List, Literal, NewType, Optional, Pattern, Union

from .element import Tag

Filter = Union[AnyStr, List[AnyStr], Pattern, Callable[[Tag], bool], Literal[True]]

ResultSetType = NewType("ResultSetType", List[Tag])
