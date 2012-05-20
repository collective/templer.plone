from setuptools import setup, find_packages
import os

version = '1.0b1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

tests_require = [
    'Cheetah',
    'PasteScript',
    'templer.core',
    'templer.buildout',
    'templer.zope',
]

localcommands_require = [
    'templer.plone.localcommands',
]

setup(name='templer.plone',
      version=version,
      description="Templer system extensions for plone add-on development",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Development Status :: 4 - Beta",
          "Framework :: Zope2",
          "Framework :: Zope3",
          "Framework :: Plone",
          "Framework :: Plone :: 3.2",
          "Framework :: Plone :: 3.3",
          "Framework :: Plone :: 4.0",
          "Framework :: Plone :: 4.1",
          "Framework :: Buildout",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          'Programming Language :: Python :: 2.4',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
          "Topic :: Software Development :: Code Generators",
        ],
      keywords='zope buildout plone',
      author='Cris Ewing',
      author_email='cris@crisewing.com',
      url='http://svn.plone.org/svn/collective/templer.plone',
      license='MIT',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['templer'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'templer.core',
          'templer.buildout',
          'templer.zope',
      ],
      tests_require=tests_require,
      extras_require=dict(test=tests_require,
                          localcommands=localcommands_require),
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      plone_basic = templer.plone:Plone
      plone_nested = templer.plone:NestedPlone
      archetype = templer.plone:Archetype

      [templer.templer_structure]
      namespace_profile = templer.plone.structures:ProfileStructure
      nested_namespace_profile = templer.plone.structures:NestedProfileStructure
      """,
      )
