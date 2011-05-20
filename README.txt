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

Other Functions
---------------

The ``templer`` script provides a number of other functions, these are described
in full on the index page for templer.core_ at PyPI_

.. _templer.core: http://pypi.python.org/pypi/templer.core
.. _PyPI: http://pypi.python.org/pypi
