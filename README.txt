.. contents::

Introduction
============

This package extends the functionality of the templer code generation system.
It builds upon the functionality of templer.core_, templer.buildout_ and 
templer.zope_, and depends on those packages. This package provides basic 
support for creating plone add-ons. Included are templates for basic plone 
packages, nested namespace plone packages and archetypes plone packages.

.. _templer.core: http://pypi.python.org/pypi/templer.core
.. _templer.buildout: http://pypi.python.org/pypi/templer.buildout
.. _templer.zope: http://pypi.python.org/pypi/templer.zope

Creating Packages
-----------------

As with the parent package, templer.core, creating packages using
templer.plone templates is accomplished by using the ``templer`` script. The
script is invoked thus::

    templer plone_basic

This will create a basic plone package skeleton.

Migration from ZopeSkel
-------------------------

Templer cannot coexist with old ZopeSkel in the same buildout, or Python virtualenv. 

Otherwise you will encounter the following error when trying to create packages::

      IOError: No egg-info directory found (looked in ./mycompany.content/./mycompany.content.egg-info, ./mycompany.content/bootstrap.py/mycompany.content.egg-info, ./mycompany.content/buildout.cfg/mycompany.content.egg-info, ./mycompany.content/CHANGES.txt/mycompany.content.egg-info, ./mycompany.content/CONTRIBUTORS.txt/mycompany.content.egg-info, ./mycompany.content/docs/mycompany.content.egg-info, ./mycompany.content/MANIFEST.in/mycompany.content.egg-info, ./mycompany.content/mycompany/mycompany.content.egg-info, ./mycompany.content/Paste-1.7.5.1-py2.6.egg/mycompany.content.egg-info, ./mycompany.content/PasteDeploy-1.5.0-py2.6.egg/mycompany.content.egg-info, ./mycompany.content/PasteScript-1.7.5-py2.6.egg/mycompany.content.egg-info, ./mycompany.content/README.txt/mycompany.content.egg-info, ./mycompany.content/setup.cfg/mycompany.content.egg-info, ./mycompany.content/setup.py/mycompany.content.egg-info, ./mycompany.content/src/mycompany.content.egg-info)

Before start using Templer

* Remove ZopeSkel references in buildout.cfg

* rm -rf eggs/ZopeSkel*

Other Functions
---------------

The ``templer`` script provides a number of other functions, these are described
in full on the index page for templer.core_ at PyPI_

.. _templer.core: http://pypi.python.org/pypi/templer.core
.. _PyPI: http://pypi.python.org/pypi
