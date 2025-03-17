#!/usr/bin/env python3

from setuptools import setup

setup(
	name='etag_generator',
	version='0.1.0',
	description='Given a JSON object (python dict), generate a stable value suitable as an ETag',
	url='https://github.com/paulprogrammer/py-json-etag-generator',
	author='Paul Williams',
	author_email='paul_williams@epam.com',
	license='Apache 2.0',
	packages=['src/etag_generator'],
	install_requires=[],

	classifiers=[
		'Development Status :: 1 - Planning',
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: Apache Software License',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3 :: Only',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Utilities'
	]
)