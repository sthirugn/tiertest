"""Helper module"""
import unittest


def createSuite(tier):
    caseList = []
    for testcase in tier:
        testSuite = unittest.TestLoader().loadTestsFromTestCase(testcase)
        caseList.append(testSuite)
    # Create new test suite
    return unittest.TestSuite(caseList)
