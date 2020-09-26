Execution/Evaluation
====================

 * Finish library search path
 * Strip white space from stack trace
 * Implement ``@`` for accessing the global scope
 * Finish adding ability to load rollit libraries from python files
 * Finish implementing the ``*`` special accessor

Tests
=====

 * Add tests for error handling (``attempt``, ``oops``, etcetera)
 * Add tests for standard library

Parsing/AST
===========

 * Add prefix the string literals that will strip whitespace before after newlines

Standard Library
================

rootlib
-------

Modifiers
^^^^^^^^^

 * input

bags
----
 * set default
 * pop

os
--

 * cli args

io
--

Bags
^^^^

 * Finish File bag

Other
^^^^^

 * path stuff

rolls
-----

 * insert element into a roll
 * slice a roll
 * sort

dnd5e
-----

Bags
^^^^
 * Ability Score
 * Skill
 * Stat block
 * Initiative tracker

Other
^^^^^

 * Advantage
 * Disadvantage

Documentation
=============

* ALL of it

Extra
=====

* Finish pygments lexer
* Rework vim plugin
