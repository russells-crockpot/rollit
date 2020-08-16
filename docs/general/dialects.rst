.. _Dialects:

Dialects
********

Dialects are a way for you to add or override different modifiers for different situations. Going
back to the example in :ref:`Notation | Substitutions`, having an ``advantage`` substitution makes
perfect sense in D&D 5th Edition, but less sense in Pathfinder, which doesn't have a concept of
advantage or disadvantage. Therefore, it makes sense to be able to separate them.

Additionally, a dialect can inherit from another dialect.

.. _Dialects | Defining Dialects:

Defining Dialects
=================

There are two ways to define a dialect: via the python API or via a dialect definition file.


.. _Dialects | Dialect Definition File:

Dialect Definition File
-----------------------

One or more dialect can be defined via a single yaml file.

TODO
