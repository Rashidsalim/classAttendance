# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in class_attendance/__init__.py
from class_attendance import __version__ as version

setup(
	name='class_attendance',
	version=version,
	description='Lecture Module',
	author='s',
	author_email='s',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
