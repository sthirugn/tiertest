tiertest
========

This a sample repository to demonstrate tier tests.

The tier tests can be run by calling the corresponding modules::

  $ python tier1.py
  ..
  ----------------------------------------------------------------------
  Ran 2 tests in 0.000s
  
  OK
  
  $ python tier2.py
  ..
  ----------------------------------------------------------------------
  Ran 2 tests in 0.000s
  
  OK
  
  $ python tier3.py
  ..
  ----------------------------------------------------------------------
  Ran 2 tests in 0.000s

  OK

Advantages:
==========

1. The tests are independent of the tier definitions.
2. The tier tests can be added/deleted in any tier easily without actually
   modifying any tests.
3. This approach will prevent the usage of nosetests attr or pytest mark which
   will  make robottelo test runner dependent.
4. These tier tests can also be run using nosetests or pytest locally.

