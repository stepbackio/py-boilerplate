#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""


import os
# Always prefer setuptools over distutils
from setuptools import setup, Command, find_packages
# To use a consistent encoding
from codecs import open

base_dir = os.path.dirname(__file__)
here = os.path.abspath(base_dir)

# include all templates in data folder
# def get_data_files(filename):
#     if not os.path.isdir(filename):
#         if filename.endswith('.tp'):
#             return os.path.join(here, 'data', filename)
#
# data_files = map(get_data_files,
#                  os.listdir(here + '/data'))
# print data_files

about = {}
with open(os.path.join(base_dir, "project", "__about__.py")) as f:
    exec(f.read(), about)

# Get the long description from the README file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


# include all templates and ocio configs in data folder
data_files = [(root.replace(here + '/data', 'data/' + about['__title__']),
               [os.path.join(root, data_file) for data_file in files])
              for root, dirs, files in os.walk(here + '/data')]


class wrap_binary(Command):
    """
    Build lib
    Install data
    Build doc
    Build bin
    """
    description = "custom wrap_binary command"
    user_options = [('build-dst=', None, 'path to Dist lib'), ]

    def initialize_options(self):
        self.cwd = None
        self.build_dst = None

    def finalize_options(self):
        self.cwd = os.getcwd()

    def run(self):
        assert os.getcwd() == self.cwd, 'Must be in package root: %s' % self.cwd

        if self.build_dst:
            print(self.build_dst)
            src = os.path.abspath('compo')
            dst = os.path.join(self.build_dst, 'compo')
            os.symlink(src, dst)
            print('compo', dst, "os.symlink(item, dst)")


class build_all(Command):
    """
    Build lib
    Install data
    Build doc
    Build bin
    """
    description = "custom build_all command"
    user_options = [('build-dst=', None, 'path to Dist lib'), ]

    def initialize_options(self):
        self.cwd = None
        self.build_dst = None

    def finalize_options(self):
        self.cwd = os.getcwd()

    def run(self):
        assert os.getcwd() == self.cwd, 'Must be in package root: %s' % self.cwd

        if self.build_dst:
            print(self.build_dst)
            src = os.path.abspath('compo')
            dst = os.path.join(self.build_dst, 'compo')
            os.symlink(src, dst)
            print('compo', dst, "os.symlink(item, dst)")


class link_lib(Command):
    description = "custom link_lib command"
    user_options = [('build-dst=', None, 'path to Dist lib'), ]

    def initialize_options(self):
        self.cwd = None
        self.build_dst = None

    def finalize_options(self):
        self.cwd = os.getcwd()

    def run(self):
        assert os.getcwd() == self.cwd, 'Must be in package root: %s' % self.cwd

        if self.build_dst:
            print(self.build_dst)
            src = os.path.abspath('compo')
            dst = os.path.join(self.build_dst, 'compo')
            print('\t\t', dst)
            if os.path.islink(dst):
                os.remove(dst)
            os.symlink(src, dst)
            print('compo', dst, "os.symlink(item, dst)")


setup(
      name=about['__title__'],
      # Versions should comply with PEP440.  For a discussion on single-sourcing
      # the version across setup.py and the project code, see
      # https://packaging.python.org/en/latest/single_source_version.html
      version=about['__version__'],

      description=about['__summary__'],
      long_description=long_description,

      # The project's main homepage.
      url=about['__uri__'],

      # Author details
      author=about['__author__'],
      author_email=about['__email__'],
      # Choose your license
      license=about['__license__'],

      # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
                   # How mature is this project? Common values are
                   #   3 - Alpha
                   #   4 - Beta
                   #   5 - Production/Stable
                   'Development Status :: 3 - Alpha',

                   # Indicate who your project is intended for
                   'Intended Audience :: Developers',
                   'Topic :: Software Development :: Build Tools',

                   # Pick your license as you wish (should match "license" above)
                   about['__license__'],

                   # Specify the Python versions you support here.
                   # In particular, ensure that you indicate whether
                   # you support Python 2, Python 3 or both.
                   'Programming Language :: Python :: 3',
                   ],
      # What does your project relate to?
      keywords='sample setuptools development',

      # You can just specify the packages manually here if your project is
      # simple. Or you can use find_packages().
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      # Alternatively, if you want to distribute just a my_module.py, uncomment
      # this:
      #   py_modules=["my_module"],

      # List run-time dependencies here.  These will be installed by pip when
      # your project is installed. For an analysis of "install_requires" vs pip's
      # requirements files see:
      # https://packaging.python.org/en/latest/requirements.html
      #     install_requires=['peppercorn'],
      #       dependency_links=[],
      # install_requires=[],
      # List additional groups of dependencies here (e.g. development
      # dependencies). You can install these using the following syntax,
      # for example:
      # $ pip install -e .[dev,test]
      #     extras_require={
      #         'dev': ['check-manifest'],
      #         'test': ['coverage'],
      #     },

      # If there are data files included in your packages that need to be
      # installed, specify them here.  If using Python 2.6 or less, then these
      # have to be included in MANIFEST.in as well.
      #     package_data={
      #         __title__: ['package_data.dat'],
      #     },
      # data_files=[('data/' + about['__title__'], data_files)],
      data_files=data_files,
      cmdclass={'link_lib': link_lib},
      # Although 'package_data' is the preferred approach, in some case you may
      # need to place data files outside of your packages. See:
      # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
      # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
      #     data_files=[('my_data', ['data/data_file'])],
      # To provide executable scripts, use entry points in preference to the
      # "scripts" keyword. Entry points provide cross-platform support and allow
      # pip to create the appropriate form of executable for the target platform.
      #     entry_points={
      #         'console_scripts': [
      #             __title__ + '=' + __title__ +':main',
      #         ],
      #     },
)
