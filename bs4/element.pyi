"""
This type stub file was generated by pyright.
"""

import re
import sys
from typing import Any, Dict, List, Optional, Generator

from .auxiliary_typing import Filter

__license__ = "MIT"
DEFAULT_OUTPUT_ENCODING = "utf-8"
PY3K = sys.version_info[0] > 2
nonwhitespace_re = re.compile(r"\S+")
whitespace_re = re.compile(r"\s+")

def _alias(attr):
    """Alias one attribute name to another for backward compatibility"""
    ...

class NamespacedAttribute(str):
    def __new__(
        cls, prefix, name: Optional[Any] = ..., namespace: Optional[Any] = ...
    ): ...

class AttributeValueWithCharsetSubstitution(str):
    """A stand-in object for a character encoding specified in HTML."""

    ...

class CharsetMetaAttributeValue(AttributeValueWithCharsetSubstitution):
    """A generic stand-in for the value of a meta tag's 'charset' attribute.

    When Beautiful Soup parses the markup '<meta charset="utf8">', the
    value of the 'charset' attribute will be one of these objects.
    """

    def __new__(cls, original_value): ...
    def encode(self, encoding): ...

class ContentMetaAttributeValue(AttributeValueWithCharsetSubstitution):
    """A generic stand-in for the value of a meta tag's 'content' attribute.

    When Beautiful Soup parses the markup:
     <meta http-equiv="content-type" content="text/html; charset=utf8">

    The value of the 'content' attribute will be one of these objects.
    """

    CHARSET_RE = ...
    def __new__(cls, original_value): ...
    def encode(self, encoding): ...

class PageElement(object):
    """Contains the navigational information for some part of the page
    (either a tag or a piece of text)"""

    def setup(
        self,
        parent: Optional[Any] = ...,
        previous_element: Optional[Any] = ...,
        next_element: Optional[Any] = ...,
        previous_sibling: Optional[Any] = ...,
        next_sibling: Optional[Any] = ...,
    ):
        """Sets up the initial relations between this element and
        other elements."""
        self.parent = ...
        self.previous_element = ...
        self.next_element = ...
        self.next_sibling = ...
        self.previous_sibling = ...
    def format_string(self, s, formatter):
        """Format the given string using the given formatter."""
        ...
    def formatter_for_name(self, formatter):
        """Look up or create a Formatter for the given identifier,
        if necessary.

        :param formatter: Can be a Formatter object (used as-is), a
        function (used as the entity substitution hook for an
        XMLFormatter or HTMLFormatter), or a string (used to look up
        an XMLFormatter or HTMLFormatter in the appropriate registry.
        """
        ...
    @property
    def _is_xml(self):
        """Is this element part of an XML tree or an HTML tree?

        This is used in formatter_for_name, when deciding whether an
        XMLFormatter or HTMLFormatter is more appropriate. It can be
        inefficient, but it should be called very rarely.
        """
        ...
    nextSibling = ...
    previousSibling = ...
    def replace_with(self, replace_with): ...
    replaceWith = ...
    def unwrap(self): ...
    replace_with_children = ...
    replaceWithChildren = ...
    def wrap(self, wrap_inside): ...
    def extract(self):
        """Destructively rips this element out of the tree."""
        self.previous_element = ...
        self.parent = ...
        self.previous_sibling = ...
    def _last_descendant(self, is_initialized: bool = ..., accept_self: bool = ...):
        "Finds the last element beneath this object to be parsed."
        ...
    _lastRecursiveChild = ...
    def insert(self, position, new_child): ...
    def append(self, tag):
        """Appends the given tag to the contents of this tag."""
        ...
    def extend(self, tags):
        """Appends the given tags to the contents of this tag."""
        ...
    def insert_before(self, *args):
        """Makes the given element(s) the immediate predecessor of this one.

        The elements will have the same parent, and the given elements
        will be immediately before this one.
        """
        ...
    def insert_after(self, *args):
        """Makes the given element(s) the immediate successor of this one.

        The elements will have the same parent, and the given elements
        will be immediately after this one.
        """
        ...
    def find_next(
        self, name: Optional[Any] = ..., attrs=..., text: Optional[Any] = ..., **kwargs
    ):
        """Returns the first item that matches the given criteria and
        appears after this Tag in the document."""
        ...
    findNext = ...
    def find_all_next(
        self,
        name: Optional[Any] = ...,
        attrs=...,
        text: Optional[Any] = ...,
        limit: Optional[Any] = ...,
        **kwargs
    ):
        """Returns all items that match the given criteria and appear
        after this Tag in the document."""
        ...
    findAllNext = ...
    def find_next_sibling(
        self, name: Optional[Any] = ..., attrs=..., text: Optional[Any] = ..., **kwargs
    ):
        """Returns the closest sibling to this Tag that matches the
        given criteria and appears after this Tag in the document."""
        ...
    findNextSibling = ...
    def find_next_siblings(
        self,
        name: Optional[Any] = ...,
        attrs=...,
        text: Optional[Any] = ...,
        limit: Optional[Any] = ...,
        **kwargs
    ):
        """Returns the siblings of this Tag that match the given
        criteria and appear after this Tag in the document."""
        ...
    findNextSiblings = ...
    fetchNextSiblings = ...
    def find_previous(
        self, name: Optional[Any] = ..., attrs=..., text: Optional[Any] = ..., **kwargs
    ):
        """Returns the first item that matches the given criteria and
        appears before this Tag in the document."""
        ...
    findPrevious = ...
    def find_all_previous(
        self,
        name: Optional[Any] = ...,
        attrs=...,
        text: Optional[Any] = ...,
        limit: Optional[Any] = ...,
        **kwargs
    ):
        """Returns all items that match the given criteria and appear
        before this Tag in the document."""
        ...
    findAllPrevious = ...
    fetchPrevious = ...
    def find_previous_sibling(
        self, name: Optional[Any] = ..., attrs=..., text: Optional[Any] = ..., **kwargs
    ):
        """Returns the closest sibling to this Tag that matches the
        given criteria and appears before this Tag in the document."""
        ...
    findPreviousSibling = ...
    def find_previous_siblings(
        self,
        name: Optional[Any] = ...,
        attrs=...,
        text: Optional[Any] = ...,
        limit: Optional[Any] = ...,
        **kwargs
    ):
        """Returns the siblings of this Tag that match the given
        criteria and appear before this Tag in the document."""
        ...
    findPreviousSiblings = ...
    fetchPreviousSiblings = ...
    def find_parent(self, name: Optional[Any] = ..., attrs=..., **kwargs):
        """Returns the closest parent of this Tag that matches the given
        criteria."""
        ...
    findParent = ...
    def find_parents(
        self, name: Optional[Any] = ..., attrs=..., limit: Optional[Any] = ..., **kwargs
    ):
        """Returns the parents of this Tag that match the given
        criteria."""
        ...
    findParents = ...
    fetchParents = ...
    @property
    def next(self): ...
    @property
    def previous(self): ...
    def _find_one(self, method, name, attrs, text, **kwargs): ...
    def _find_all(self, name, attrs, text, limit, generator, **kwargs):
        "Iterates over a generator looking for things that match."
        ...
    @property
    def next_elements(self): ...
    @property
    def next_siblings(self): ...
    @property
    def previous_elements(self): ...
    @property
    def previous_siblings(self): ...
    @property
    def parents(self): ...
    def nextGenerator(self): ...
    def nextSiblingGenerator(self): ...
    def previousGenerator(self): ...
    def previousSiblingGenerator(self): ...
    def parentGenerator(self): ...

class NavigableString(str, PageElement):
    PREFIX = ...
    SUFFIX = ...
    known_xml = ...
    def __new__(cls, value):
        """Create a new NavigableString.

        When unpickling a NavigableString, this method is called with
        the string in DEFAULT_OUTPUT_ENCODING. That encoding needs to be
        passed in to the superclass's __new__ or the superclass won't know
        how to handle non-ASCII characters.
        """
        ...
    def __copy__(self):
        """A copy of a NavigableString has the same contents and class
        as the original, but it is not connected to the parse tree.
        """
        ...
    def __getnewargs__(self): ...
    def __getattr__(self, attr):
        """text.string gives you text. This is for backwards
        compatibility for Navigable*String, but for CData* it lets you
        get the string without the CData wrapper."""
        ...
    def output_ready(self, formatter=...):
        """Run the string through the provided formatter."""
        ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name): ...

class PreformattedString(NavigableString):
    """A NavigableString not subject to the normal formatting rules.

    The string will be passed into the formatter (to trigger side effects),
    but the return value will be ignored.
    """

    def output_ready(self, formatter: Optional[Any] = ...):
        """CData strings are passed into the formatter, purely
        for any side effects. The return value is ignored.
        """
        ...

class CData(PreformattedString):
    PREFIX = ...
    SUFFIX = ...

class ProcessingInstruction(PreformattedString):
    """A SGML processing instruction."""

    PREFIX = ...
    SUFFIX = ...

class XMLProcessingInstruction(ProcessingInstruction):
    """An XML processing instruction."""

    PREFIX = ...
    SUFFIX = ...

class Comment(PreformattedString):
    PREFIX = ...
    SUFFIX = ...

class Declaration(PreformattedString):
    PREFIX = ...
    SUFFIX = ...

class Doctype(PreformattedString):
    @classmethod
    def for_name_and_ids(cls, name, pub_id, system_id): ...
    PREFIX = ...
    SUFFIX = ...

class Tag(PageElement):
    """Represents a found HTML tag with its attributes and contents."""

    def __init__(
        self,
        parser: Optional[Any] = ...,
        builder: Optional[Any] = ...,
        name: Optional[Any] = ...,
        namespace: Optional[Any] = ...,
        prefix: Optional[Any] = ...,
        attrs: Optional[Any] = ...,
        parent: Optional[Any] = ...,
        previous: Optional[Any] = ...,
        is_xml: Optional[Any] = ...,
        sourceline: Optional[Any] = ...,
        sourcepos: Optional[Any] = ...,
        can_be_empty_element: Optional[Any] = ...,
        cdata_list_attributes: Optional[Any] = ...,
        preserve_whitespace_tags: Optional[Any] = ...,
    ):
        "Basic constructor."
        self.name = ...
        self.namespace = ...
        self.prefix = ...
        self.attrs = ...
        self.contents = ...
        self.hidden = ...
    parserClass = ...
    def __copy__(self):
        """A copy of a Tag is a new Tag, unconnected to the parse tree.
        Its contents are a copy of the old Tag's contents.
        """
        ...
    @property
    def is_empty_element(self):
        """Is this tag an empty-element tag? (aka a self-closing tag)

        A tag that has contents is never an empty-element tag.

        A tag that has no contents may or may not be an empty-element
        tag. It depends on the builder used to create the tag. If the
        builder has a designated list of empty-element tags, then only
        a tag whose name shows up in that list is considered an
        empty-element tag.

        If the builder has no designated list of empty-element tags,
        then any tag with no contents is an empty-element tag.
        """
        ...
    isSelfClosing = ...
    @property
    def string(self):
        """Convenience property to get the single string within this tag.

        :Return: If this tag has a single string child, return value
         is that string. If this tag has no children, or more than one
         child, return value is None. If this tag has one child tag,
         return value is the 'string' attribute of the child tag,
         recursively.
        """
        ...
    @string.setter
    def string(self, string): ...
    def _all_strings(self, strip: bool = ..., types=...):
        """Yield all strings of certain classes, possibly stripping them.

        By default, yields only NavigableString and CData objects. So
        no comments, processing instructions, etc.
        """
        ...
    strings = ...
    @property
    def stripped_strings(self): ...
    def get_text(self, separator=..., strip: bool = ..., types=...):
        """
        Get all child strings, concatenated using the given separator.
        """
        ...
    getText = ...
    text = ...
    def decompose(self):
        """Recursively destroys the contents of this tree."""
        ...
    def clear(self, decompose: bool = ...):
        """
        Extract all children. If decompose is True, decompose instead.
        """
        ...
    def smooth(self):
        """Smooth out this element's children by consolidating consecutive strings.

        This makes pretty-printed output look more natural following a
        lot of operations that modified the tree.
        """
        ...
    def index(self, element):
        """
        Find the index of a child by identity, not value. Avoids issues with
        tag.contents.index(element) getting the index of equal elements.
        """
        ...
    def get(self, key, default: Optional[Any] = ...):
        """Returns the value of the 'key' attribute for the tag, or
        the value given for 'default' if it doesn't have that
        attribute."""
        ...
    def get_attribute_list(self, key, default: Optional[Any] = ...):
        """The same as get(), but always returns a list."""
        ...
    def has_attr(self, key): ...
    def __hash__(self): ...
    def __getitem__(self, key):
        """tag[key] returns the value of the 'key' attribute for the tag,
        and throws an exception if it's not there."""
        ...
    def __iter__(self):
        "Iterating over a tag iterates over its contents."
        ...
    def __len__(self):
        "The length of a tag is the length of its list of contents."
        ...
    def __contains__(self, x): ...
    def __bool__(self):
        "A tag is non-None even if it has no contents."
        ...
    def __setitem__(self, key, value):
        """Setting tag[key] sets the value of the 'key' attribute for the
        tag."""
        ...
    def __delitem__(self, key):
        "Deleting tag[key] deletes all 'key' attributes for the tag."
        ...
    def __call__(self, *args, **kwargs):
        """Calling a tag like a function is the same as calling its
        find_all() method. Eg. tag('a') returns a list of all the A tags
        found within this tag."""
        ...
    def __getattr__(self, tag): ...
    def __eq__(self, other):
        """Returns true iff this tag has the same name, the same attributes,
        and the same contents (recursively) as the given tag."""
        ...
    def __ne__(self, other):
        """Returns true iff this tag is not identical to the other tag,
        as defined in __eq__."""
        ...
    def __repr__(self, encoding=...):
        """Renders this tag as a string."""
        ...
    def __unicode__(self): ...
    def __str__(self): ...
    if PY3K:
        __str__ = ...
    def encode(
        self, encoding=..., indent_level: Optional[Any] = ..., formatter=..., errors=...
    ): ...
    def decode(
        self, indent_level: Optional[Any] = ..., eventual_encoding=..., formatter=...
    ):
        """Returns a Unicode representation of this tag and its contents.

        :param eventual_encoding: The tag is destined to be
           encoded into this encoding. This method is _not_
           responsible for performing that encoding. This information
           is passed in so that it can be substituted in if the
           document contains a <META> tag that mentions the document's
           encoding.
        """
        ...
    def _should_pretty_print(self, indent_level):
        """Should this tag be pretty-printed?"""
        ...
    def prettify(self, encoding: Optional[Any] = ..., formatter=...): ...
    def decode_contents(
        self, indent_level: Optional[Any] = ..., eventual_encoding=..., formatter=...
    ):
        """Renders the contents of this tag as a Unicode string.

        :param indent_level: Each line of the rendering will be
           indented this many spaces.

        :param eventual_encoding: The tag is destined to be
           encoded into this encoding. decode_contents() is _not_
           responsible for performing that encoding. This information
           is passed in so that it can be substituted in if the
           document contains a <META> tag that mentions the document's
           encoding.

        :param formatter: A Formatter object, or a string naming one of
            the standard Formatters.
        """
        ...
    def encode_contents(
        self, indent_level: Optional[Any] = ..., encoding=..., formatter=...
    ):
        """Renders the contents of this tag as a bytestring.

        :param indent_level: Each line of the rendering will be
           indented this many spaces.

        :param eventual_encoding: The bytestring will be in this encoding.

        :param formatter: The output formatter responsible for converting
           entities to Unicode characters.
        """
        ...
    def renderContents(
        self, encoding=..., prettyPrint: bool = ..., indentLevel=...
    ): ...
    def find(
        self,
        name: Optional[Filter] = ...,
        attrs: Dict[str, Filter] = ...,
        recursive: bool = ...,
        text: Optional[Filter] = ...,
        **kwargs: Filter
    ) -> Optional[Tag]:
        """Return only the first child of this Tag matching the given
        criteria."""
        ...
    findChild = ...
    def find_all(
        self,
        name: Optional[Filter] = ...,
        attrs: Dict[str, Filter] = ...,
        recursive: bool = ...,
        text: Optional[Filter] = ...,
        limit: Optional[int] = ...,
        **kwargs: Filter
    ) -> "ResultSet":
        """Extracts a list of Tag objects that match the given
        criteria.  You can specify the name of the Tag and any
        attributes you want the Tag to have.

        The value of a key-value pair in the 'attrs' map can be a
        string, a list of strings, a regular expression object, or a
        callable that takes a string and returns whether or not the
        string matches for some custom definition of 'matches'. The
        same is true of the tag name."""
        ...
    findAll = ...
    findChildren = ...
    @property
    def children(self): ...
    @property
    def descendants(self): ...
    def select_one(self, selector, namespaces: Optional[Any] = ..., **kwargs):
        """Perform a CSS selection operation on the current element."""
        ...
    def select(
        self,
        selector,
        namespaces: Optional[Any] = ...,
        limit: Optional[Any] = ...,
        **kwargs
    ):
        """Perform a CSS selection operation on the current element.

        This uses the SoupSieve library.

        :param selector: A string containing a CSS selector.

        :param namespaces: A dictionary mapping namespace prefixes
        used in the CSS selector to namespace URIs. By default,
        Beautiful Soup will use the prefixes it encountered while
        parsing the document.

        :param limit: After finding this number of results, stop looking.

        :param kwargs: Any extra arguments you'd like to pass in to
        soupsieve.select().
        """
        ...
    def childGenerator(self): ...
    def recursiveChildGenerator(self): ...
    def has_key(self, key):
        """This was kind of misleading because has_key() (attributes)
        was different from __in__ (contents). has_key() is gone in
        Python 3, anyway."""
        ...

class SoupStrainer(object):
    """Encapsulates a number of ways of matching a markup element (tag or
    text)."""

    def __init__(
        self, name: Optional[Any] = ..., attrs=..., text: Optional[Any] = ..., **kwargs
    ):
        self.name = ...
        self.attrs = ...
        self.text = ...
    def _normalize_search_value(self, value): ...
    def __str__(self): ...
    def search_tag(self, markup_name: Optional[Any] = ..., markup_attrs=...): ...
    searchTag = ...
    def search(self, markup): ...
    def _matches(self, markup, match_against, already_tried: Optional[Any] = ...): ...

class ResultSet(list):
    """A ResultSet is just a list that keeps track of the SoupStrainer
    that created it."""

    def __init__(self, source: SoupStrainer, result: Generator[Tag] = ...) -> None:
        self.source = ...
    def __getattr__(self, key): ...
