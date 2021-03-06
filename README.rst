.. image:: https://badge.fury.io/py/morning.png
    :target: http://badge.fury.io/py/morning

.. image:: https://travis-ci.org/Carreau/morning.png?branch=master
        :target: https://travis-ci.org/Carreau/morning

.. image:: https://pypip.in/d/morning/badge.png
        :target: https://pypi.python.org/pypi/morning


Morning is a package that should (at some point in the future) deals with all the updates I need to do
in the morning on my computer. That is to say :

    - Fetch all the git repos I'm working on. 
    - Make sure they are on master:
        - If they are, and can be fast-forwarded, do it and potentially asking me wether or not

installing morning
------------------

.. note::

    I'm using Python 3.5 HEAD, and I plan to try to use subprocess.run, so it might not run for you. 

.. code::
    pip install morning


Using morning
-------------

.. code::

    $ cd this/is/a/git/backed/project
    $ mornign add . 
    adding /Users/bussonniermatthias/this/is/a/git/backed/project to list of git repos to update

.. code::

    $ morning list
    /users/bussonniermatthias/dev/flit
    /users/bussonniermatthias/dev/ipython
    /users/bussonniermatthias/dev/ipython_genutils
    /users/bussonniermatthias/dev/ipython_kernel
    /users/bussonniermatthias/dev/jupyter_client
    /users/bussonniermatthias/dev/jupyter_core
    /users/bussonniermatthias/dev/jupyter_nbconvert
    /users/bussonniermatthias/dev/jupyter_nbformat
    /users/bussonniermatthias/dev/jupyter_notebook
    /users/bussonniermatthias/dev/morning
    /users/bussonniermatthias/dev/brackets-visualtabs




Updating all these git repos:

.. code::
    $ morning


# auto-fast-forward

use the following to tell morning to automatically
fast forward your repo if on master, and behind origin.

.. code::

    $ git config morning.fast-forward True


End Target:
-----------


How it should look like:

.. code::
    ~/dev $ morning
            dev/nikola  |  master | -76
            Would you like to git reset origin/master[y/N]?
            .... # probably yes
            dev/ipython |  master | -76,+17
            Would you like to git reset origin/master[y/N]?
            .... # I probably have unpushed changes.


Maybe it should also have custom hooks to update homebrew, or alike. Maybe a `morning add .` would be nice to track a specific component, and also a way to provide a command to run pre/post checkout. (can do that with git hooks)

Local configuration would be in .git/config in the `[morning]` section. 


* Free software: BSD license
* Documentation: https://morning.readthedocs.org.

TODO
----

Use flit for installation


