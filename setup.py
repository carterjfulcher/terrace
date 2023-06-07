import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
  name='terrace',
  version='1.0.0',
  url='https://github.com/carterjfulcher/terrace',
  author='carterjfulcher',
  author_email='carter@fulcheranalytics.io',
  packages=find_packages(exclude=("tests",)),
  platforms='any',
  license='MIT',
  ext_modules=[],
  description="an open source algorithmic trading engine optimized for a great developer experience",
  long_description='See https://github.com/carterjfulcher/terrace',
)