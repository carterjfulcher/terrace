import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
  name='terrace',
  version='0.0.1',
  url='https://github.com/carterjfulcher/terrace',
  author='carterjfulcher',
  author_email='carter@fulcheranalytics.io',
  packages=find_packages(exclude=("tests",)),
  platforms='any',
  license='MIT',
  ext_modules=[],
  description="Open source platform for financial index creation, management, and operation",
  long_description='See https://github.com/carterjfulcher/terrace',
)