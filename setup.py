from setuptools import setup, find_packages
import os.path
import re

# reading package's version (same way sqlalchemy does)
with open(
    os.path.join(os.path.dirname(__file__), 'excel_to_database', '__init__.py')
) as v_file:
    package_version = \
        re.compile('.*__version__ = \'(.*?)\'', re.S)\
        .match(v_file.read())\
        .group(1)




setup(
    name='vip_adimin',
    version=package_version,
    author='Mohamad Khajezade',
    author_email='khajezade.mohamad@gmail.com',
    description='A package to read excel file and save it to database',
    packages=find_packages()
)
