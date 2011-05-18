.. contents::

Introduction
============

This package extends the functionality of the templer code generation system.
It builds upon the functionality of templer.core_ and templer.buildout_, and
depends on those packages. This package provides basic support for creating
zope packages and zope buildouts. Included are packages for basic plone 
packages, nested namespace plone packages and plone buildouts.

.. _templer.core: http://pypi.python.org/pypi/templer.core
.. _templer.buildout: http://pypi.python.org/pypi/templer.buildout

Creating Packages
-----------------

As with the parent package, templer.core, creating packages using
templer.zope templates is accomplished by using the ``templer`` script. The
script is invoked thus::

    templer basic_zope

This will create a basic zope package skeleton.

Other Functions
---------------

The ``templer`` script provides a number of other functions, these are described
in full on the index page for templer.core_ at PyPI_

.. _templer.core: http://pypi.python.org/pypi/templer.core
.. _PyPI: http://pypi.python.org/pypi
