.. _Types:

Types
=====

.. _Types | int and float:

int and float
-------------

As you can probably guess from the name, these are both number based primitives, with ``int`` being
and integer and ``float`` being a floating point number.

.. _Types | dice:

dice
----

A ``dice`` object is more or less what you would expect: the dice to use in a roll. For example,
``1d6`` would define a ``dice``. A more complex example would be:

>>> (2d(3d4) + 6)d((2d3)d(6d4)+5)

Here you have multiple embedded dice, but the expression itself evaluates to a ``dice``. ``dice``
can be rolled via a :ref:`Expressions | roll` expression, or a :ref:`Expressions | pack`
expression, both of which will provide you with a :ref:`Types | result`.

A ``dice`` has two attributes:

:number_of_dice: The number of dice that this roll has. This can also be retrieved by using a
                 :ref:`Expressions | length` expression.

:sides: The number of sides the dice have.

.. admonition:: That name, though...

   Yeah, using a plural word as a singular bugs me, too. Unfortunately I couldn't come up with a
   better one. I thought about using ``roll``, but decided that may only cause confusion. I am
   :bolditalic:`more` than willing to hear suggestions.


.. _Types | result:

result
------

A result is, simply put, the result of a :ref:`Expressions | roll` (or a :ref:`Expressions | pack`).
A result object has three different attributes that can be accessed via a
:ref:`Expressions | access` expression. They are:

.. _Types | result | rolls:

:rolls: A list with the results of the rolls. This result is mutable.

.. _Types | result | total:

:total: The summed total of all of the :ref:`rolls <Types | result | rolls>`. This value is
        automatically generated and cannot be changed directly (although it can be changed by
        changing the :ref:`rolls <Types | result | rolls>`).

.. _Types | result | value:

:value: By default, this is the same as the :ref:`total <Types | result | total>`; however it is
        mutable and can be set. When ``result``\s need to be treated as a single number, this is the
        value used.

One thing that can be complicated about ``result``\s is their determinism. While you would expect
the result object's attributes to be the same every time they're evaluated, this isn't necessarily
the case. If the :ref:`value <Types | result | value>` or any of the
:ref:`rolls <Types | result | rolls>` are a :ref:`Types | dice` then those dice will be re-rolled
every time. To prevent this, use a :ref:`Expressions | freeze` expression.

When a :ref:`Expressions | length` expression is used on the result, the number of objects in the
:ref:`rolls <Types | result | rolls>` will be returned. Individual rolls can be retrieved by using
subscript on the :ref:`rolls <Types | result | rolls>` attribute or on the result itself.


.. _Types | modifier:

modifier
--------


.. _Types | macro:

macro
-----
