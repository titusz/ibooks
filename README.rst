============================================================
ibooks - Extract cover and metadata from iBooks Author files
============================================================

*"ibooks" is a small python module that can be used to extract cover images
and basic metadata from iBooks Author files.*

- **Author:** *Titusz <tp at py7 de>*
- **PyPi:** http://pypi.python.org/pypi/ibooks
- **Source Code**: http://github.com/titusz/ibooks
- **License**: BSD

Installation
------------

Use easy_install or pip::

    pip install ibooks


Commandline Usage
-----------------
With the commandline script you can print metadata to the console and extract
the cover from .ibooks files::

    ibooks my-ibooks-author-file.ibooks


Library Usage
-------------
Here is how you can use 'ibooks' as a lib in your code::

    >>>from ibooks import iBooks
    >>>ibook = iBooks('my-ibooks-author.ibooks')

    # Get some metadata
    >>> ibook.title
    "Title of iBooks file"
    >>>ibook.author
    "Authors Name"

    # Extract cover
    >>>ibook.cover
    /temp-path-to/OPS/assets/images/cover-image.jpg
    # Be sure to process the image file before the "ibook" object is released

