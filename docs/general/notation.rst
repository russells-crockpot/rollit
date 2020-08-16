.. _Notation:

########
Notation
########

Roll With It uses a super set of
`standard dice notation <https://en.wikipedia.org/wiki/Dice_notation>`_. The primary differences are
modifiers and substitutions.

.. seealso::

    :ref:`Dialects` for a list of built in and prepackaged modifiers and substitutions.

.. _Notation | Substitutions:

Substitutions
=============

Substitutions are an easy way for you to reuse certain constants. For example, in D&D 5th Edition,
you have advantage and disadvantage, which always use d20s. While you could define a modifier
named ``advantage`` that is equivalent to ``:highest(1)``, it can get tedious to always write
``d20:advantage`` when you know that the type of dice will never change. Instead, a better way would
be to define a substitution and use it. Substitutions are referenced by enclosing the substitution's
name in matching curly braces (i.e. ``{`` and ``}``). The reference will be replaced with the
*exact* text defined for the substitution's value. This will be done before any other processing of
the input occurs.

.. _Notation | Modifiers:

Modifiers
=========

Modifiers are additions to a dice roll that (surprise, surprise) modify the results. They are
defined by adding a ``:`` followed by the modifier name. Multiple modifiers can be added, although
some may conflict with others. For example:

>>> 4d6:expand


Arguments to modifiers are passed in via parentheses. For example, let's assume we have the
following example:

>>> 4d6:lowest(2)

Standard modifiers (as well as names and aliases) are explained below, as well as different
dialects.
