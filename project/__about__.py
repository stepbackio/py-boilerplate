import os.path

__all__ = ["__title__", "__summary__", "__uri__", "__version__", "__company__",
           "__author__", "__email__", "__license__", "__copyright__", ]


try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    base_dir = None


__title__ = "project"
__summary__ = "project description"
__uri__ = ""

__version__ = "0.0.0"

__company__ = "company name"
__author__ = "author"
__email__ = "user@mail.com"

__license__ = 'License :: MIT License'
__copyright__ = "2019 %s" % __company__
