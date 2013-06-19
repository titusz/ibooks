# -*- coding: utf-8 -*-
"""Read cover & metadata from iBooks files"""
import os
import shutil
from tempfile import mkdtemp
import zipfile
import xml.etree.ElementTree as etree
import sys


class iBooks(object):

    NS = {
        'opf': 'http://www.idpf.org/2007/opf',
        'dc': 'http://purl.org/dc/elements/1.1/',
    }

    IMAGE_PATH = 'OPS/assets/images/cover-image.jpg'

    def __init__(self, filepath):

        self.filepath = filepath
        self._tempdir = None
        self._extracted_cover_path = None

        with zipfile.ZipFile(self.filepath, 'r') as zipreader:
            with zipreader.open('OPS/ibooks.opf') as opf_file:
                self.opf = etree.fromstring(opf_file.read())
        self._el_meta = self.opf.find('opf:metadata', self.NS)

    @property
    def title(self):
        """Book Title as specified in metadata.

        :return str: book title
        """
        return self._el_meta.find('dc:title', self.NS).text

    @property
    def author(self):
        """Author as specified in metadata.

        :return str: author
        """
        return self._el_meta.find('dc:creator', self.NS).text

    @property
    def language(self):
        """iBook content language as specified in metadata.

        :return str: 2-letter language code
        """
        return self._el_meta.find('dc:language', self.NS).text

    @property
    def version(self):
        """Return book version.

        NOTE: iBooks Author preview files MUST not contain a version.
        :return str: version string of ibooks file
        """
        version_el = self._el_meta.find(
            "opf:meta[@property='ibooks:version']", self.NS
        )
        if version_el is not None:
            return version_el.text

    @property
    def cover(self):
        """Extract cover on first access and return full path to temporary
        cover file. Subsequent access to .cover will return cached path.

        WARNING: Temporary cover file will only exist as long as 'self' exists.
        Be sure to keep a reference to 'self' until you have processed
        the cover image.

        :return str: path to cover file
        """
        self._tempdir = self._tempdir or mkdtemp(prefix='ibooks')
        if not self._extracted_cover_path:
            with zipfile.ZipFile(self.filepath, 'r') as zipreader:
                self._extracted_cover_path = zipreader.extract(
                    self.IMAGE_PATH, self._tempdir
                )
        return self._extracted_cover_path

    def __del__(self):
        """Try to remove tempdir. We don´t care if it fails..."""
        if self._tempdir:
            shutil.rmtree(self._tempdir, ignore_errors=True)


def cli():
    """Command line script entry point.

    Prints metadata to console and extracts cover to current working directory.
    """

    try:
        ibook = iBooks(sys.argv[1])
    except:
        print('Usage:\n ibooks myfile.ibooks \n')
        return 1

    print('Title: %s' % ibook.title)
    print('Author: %s' % ibook.author)
    print('Language: %s' % ibook.language)
    print('Version: %s' % ibook.version)
    cover_path = os.path.join(
        os.getcwdu(),
        os.path.basename(sys.argv[1]).replace('.ibooks', '-cover.jpg')
    )
    shutil.copy(ibook.cover, cover_path)
    print('Extracted cover to %s' % cover_path)
    return 0
