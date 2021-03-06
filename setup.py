#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

README = \
'''
APA102 pixel ring
'''


requirements = [
    'spidev'
]

setup_requirements = [
    # TODO: put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest'
]

setup(
    name='pixel-ring',
    version='0.0.1',
    description="APA 102 pixel ring",
    long_description=README,
    author="Yihui Xiong",
    author_email='yihui.xiong@hotmail.com',
    url='https://github.com/respeaker/pixel_ring',
    packages=find_packages(include=['pixel_ring']),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
        ],
    },
    license="GNU General Public License v2",
    zip_safe=False,
    keywords='voice doa beamforming kws',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
