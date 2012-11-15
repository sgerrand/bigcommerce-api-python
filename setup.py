#!/usr/bin/env python
from setuptools import setup, find_packages
import bigcommerce

setup(
	name='bigcommerce',
	url='http://bigcommerce.com',
	version = bigcommerce.__version__,
	description='Enables Ruby applications to communicate with the BigCommerce API V2',
	author='bigcommerce',
	author_email='dev-accounts@bigcommerce.com',
	packages=find_packages(),
	license='MIT',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Software Development :: Libraries'
	],
	include_package_data = True,
	install_requires = [
		"python >= 2.3.0",
		"httplib2",
	],
)
