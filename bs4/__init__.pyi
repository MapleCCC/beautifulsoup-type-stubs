"""
This type stub file was generated by pyright.
"""

import os
import re
import sys
import traceback
import warnings
from .builder import ParserRejectedMarkup, builder_registry
from .dammit import UnicodeDammit
from .element import CData, Comment, DEFAULT_OUTPUT_ENCODING, Declaration, Doctype, NavigableString, PageElement, ProcessingInstruction, ResultSet, SoupStrainer, Tag
from typing import Any, Optional

"""Beautiful Soup
Elixir and Tonic
"The Screen-Scraper's Friend"
http://www.crummy.com/software/BeautifulSoup/

Beautiful Soup uses a pluggable XML or HTML parser to parse a
(possibly invalid) document into a tree representation. Beautiful Soup
provides methods and Pythonic idioms that make it easy to navigate,
search, and modify the parse tree.

Beautiful Soup works with Python 2.7 and up. It works better if lxml
and/or html5lib is installed.

For more than you ever wanted to know about Beautiful Soup, see the
documentation:
http://www.crummy.com/software/BeautifulSoup/bs4/doc/

"""
__author__ = "Leonard Richardson (leonardr@segfault.org)"
__version__ = "4.8.1"
__copyright__ = "Copyright (c) 2004-2019 Leonard Richardson"
__license__ = "MIT"
__all__ = ['BeautifulSoup']
class BeautifulSoup(Tag):
    """
    This class defines the basic interface called by the tree builders.

    These methods will be called by the parser:
      reset()
      feed(markup)

    The tree builder may call these methods from its feed() implementation:
      handle_starttag(name, attrs) # See note about return value
      handle_endtag(name)
      handle_data(data) # Appends to the current data node
      endData(containerClass) # Ends the current data node

    No matter how complicated the underlying parser is, you should be
    able to build a tree using 'start tag' events, 'end tag' events,
    'data' events, and "done with data" events.

    If you encounter an empty-element tag (aka a self-closing tag,
    like HTML's <br> tag), call handle_starttag and then
    handle_endtag.
    """
    ROOT_TAG_NAME = ...
    DEFAULT_BUILDER_FEATURES = ...
    ASCII_SPACES = ...
    NO_PARSER_SPECIFIED_WARNING = ...
    def __init__(self, markup=..., features: Optional[Any] = ..., builder: Optional[Any] = ..., parse_only: Optional[Any] = ..., from_encoding: Optional[Any] = ..., exclude_encodings: Optional[Any] = ..., element_classes: Optional[Any] = ..., **kwargs):
        """Constructor.

        :param markup: A string or a file-like object representing
        markup to be parsed.

        :param features: Desirable features of the parser to be used. This
        may be the name of a specific parser ("lxml", "lxml-xml",
        "html.parser", or "html5lib") or it may be the type of markup
        to be used ("html", "html5", "xml"). It's recommended that you
        name a specific parser, so that Beautiful Soup gives you the
        same results across platforms and virtual environments.

        :param builder: A TreeBuilder subclass to instantiate (or
        instance to use) instead of looking one up based on
        `features`. You only need to use this if you've implemented a
        custom TreeBuilder.

        :param parse_only: A SoupStrainer. Only parts of the document
        matching the SoupStrainer will be considered. This is useful
        when parsing part of a document that would otherwise be too
        large to fit into memory.

        :param from_encoding: A string indicating the encoding of the
        document to be parsed. Pass this in if Beautiful Soup is
        guessing wrongly about the document's encoding.

        :param exclude_encodings: A list of strings indicating
        encodings known to be wrong. Pass this in if you don't know
        the document's encoding but you know Beautiful Soup's guess is
        wrong.

        :param element_classes: A dictionary mapping BeautifulSoup
        classes like Tag and NavigableString to other classes you'd
        like to be instantiated instead as the parse tree is
        built. This is useful for using subclasses to modify the
        default behavior of Tag or NavigableString.

        :param kwargs: For backwards compatibility purposes, the
        constructor accepts certain keyword arguments used in
        Beautiful Soup 3. None of these arguments do anything in
        Beautiful Soup 4; they will result in a warning and then be ignored.

        Apart from this, any keyword arguments passed into the BeautifulSoup
        constructor are propagated to the TreeBuilder constructor. This
        makes it possible to configure a TreeBuilder beyond saying
        which one to use.

        """
        self.element_classes = ...
        self.builder = ...
        self.is_xml = ...
        self.known_xml = ...
        self.parse_only = ...
        self.markup = ...
    
    def __copy__(self):
        ...
    
    def __getstate__(self):
        ...
    
    @staticmethod
    def _check_markup_is_url(markup):
        """ 
        Check if markup looks like it's actually a url and raise a warning 
        if so. Markup can be unicode or str (py2) / bytes (py3).
        """
        ...
    
    def _feed(self):
        ...
    
    def reset(self):
        self.hidden = ...
        self.current_data = ...
        self.currentTag = ...
        self.tagStack = ...
        self.preserve_whitespace_tag_stack = ...
    
    def new_tag(self, name, namespace: Optional[Any] = ..., nsprefix: Optional[Any] = ..., attrs=..., sourceline: Optional[Any] = ..., sourcepos: Optional[Any] = ..., **kwattrs):
        """Create a new tag associated with this soup."""
        ...
    
    def new_string(self, s, subclass: Optional[Any] = ...):
        """Create a new NavigableString associated with this soup."""
        ...
    
    def insert_before(self, successor):
        ...
    
    def insert_after(self, successor):
        ...
    
    def popTag(self):
        ...
    
    def pushTag(self, tag):
        self.currentTag = ...
    
    def endData(self, containerClass: Optional[Any] = ...):
        ...
    
    def object_was_parsed(self, o, parent: Optional[Any] = ..., most_recent_element: Optional[Any] = ...):
        """Add an object to the parse tree."""
        ...
    
    def _linkage_fixer(self, el):
        """Make sure linkage of this fragment is sound."""
        ...
    
    def _popToTag(self, name, nsprefix: Optional[Any] = ..., inclusivePop: bool = ...):
        """Pops the tag stack up to and including the most recent
        instance of the given tag. If inclusivePop is false, pops the tag
        stack up to but *not* including the most recent instqance of
        the given tag."""
        ...
    
    def handle_starttag(self, name, namespace, nsprefix, attrs, sourceline: Optional[Any] = ..., sourcepos: Optional[Any] = ...):
        """Push a start tag on to the stack.

        If this method returns None, the tag was rejected by the
        SoupStrainer. You should proceed as if the tag had not occurred
        in the document. For instance, if this was a self-closing tag,
        don't call handle_endtag.
        """
        ...
    
    def handle_endtag(self, name, nsprefix: Optional[Any] = ...):
        ...
    
    def handle_data(self, data):
        ...
    
    def decode(self, pretty_print: bool = ..., eventual_encoding=..., formatter=...):
        """Returns a string or Unicode representation of this document.
        To get Unicode, pass None for encoding."""
        ...
    


_s = BeautifulSoup
_soup = BeautifulSoup
class BeautifulStoneSoup(BeautifulSoup):
    """Deprecated interface to an XML parser."""
    def __init__(self, *args, **kwargs):
        ...
    


class StopParsing(Exception):
    ...


class FeatureNotFound(ValueError):
    ...


if __name__ == '__main__':
    soup = BeautifulSoup(sys.stdin)
