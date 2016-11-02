import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from distutils.core import setup
from setuptools import find_packages, setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()

def get_readme():
    readme = ''
    try:
        import pypandoc
        readme = pypandoc.convert('README.md', 'rst')
    except (ImportError, IOError):
        with open('README.md', 'r') as file_data:
            readme = file_data.read()
    return readme

setup(name='Parseit',
      version='1.4.1',
      description="A fixed record lenght text and csv file parser",
	  long_description=get_readme(),
	  keywords='parse text file csv',
      author="Patricio Moracho",
      author_email="pmoracho@gmail.com",
      url="https://github.com/pmoracho/parseit",
	  packages=find_packages(),
      classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: Spanish',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Terminals']
)
