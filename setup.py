from io import open
from setuptools import setup

version = '0.1'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name = 'ApiCryptoPay',
    author = 'Andrew Zaycev',
    author_email = 'bonyxyq@gmail.com',
    url = 'https://github.com/andrewzaycew/cryptopayclient',
    description = 'API for CryptoBot',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    license = 'MIT',
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages = ['ApiCryptoPay'],
    where = ['where'],
    install_requires = ['requests'],
)
