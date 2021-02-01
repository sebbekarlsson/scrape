from setuptools import setup, find_packages


setup(
    name='scrape',
    version='1.0.0',
    install_requires=[
        'sqlalchemy',
        'bs4',
        'pymysql',
        'requests'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
        ]
    }
)
