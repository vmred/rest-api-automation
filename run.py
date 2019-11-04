import os
import unittest


def extend_suite(cases):
    for case in cases:
        suite.addTest(case)


suite = unittest.TestSuite()

if int(os.getenv('reqres', '1')) == 1:
    from tests.reqres.test_users import TestUsers

    extend_suite([TestUsers])

if int(os.getenvb('numbersapi', '1')) == 1:
    from tests.numbersapi.test_numbersapi import TestNumbersapi

    extend_suite([TestNumbersapi])


def run():
    unittest.TextTestRunner(verbosity=2).run(suite)
