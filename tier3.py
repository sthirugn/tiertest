# Import relevant test modules here
import unittest
# import ...
# import ...


# All tier1 test cases go here
tier3 = [
    'sampletests.test_subnet.TestSubnet.test_positive_create_5',
    'sampletests.test_subnet.TestSubnet.test_positive_create_6'
    # Add all other tests here
    # ...
    # ...
    # ...
]


def createSuite():
    new_suite = unittest.TestSuite()

    for testcase in tier3:
        testSuite = unittest.defaultTestLoader.loadTestsFromName(testcase)
        new_suite.addTest(testSuite)

    return new_suite


unittest.TextTestRunner().run(createSuite())
