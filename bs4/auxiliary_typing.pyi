from typing import AnyStr, Callable, List, Literal, Pattern, Union

from .element import Tag

Filter = Union[AnyStr, List[AnyStr], Pattern, Callable[[Tag], bool], Literal[True]]
