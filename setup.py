# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='co',
      version='0.0.1',
      description="",
      long_description=open('README.md').read(),
      classifiers=[],
      keywords='',
      author=u'Alea Soluciones',
      author_email='bifer@alea-soluciones.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'spec', 'spec.*']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[line for line in open('requirements.txt')],
      entry_points={}
)
