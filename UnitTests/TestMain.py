import unittest
import sys
import os
import subprocess

sys.path.append(os.path.abspath('..'))

from Classes import testClasses as testClass

# Test Suite
def suite():
    # Add test suites
    suitePositive = unittest.TestSuite()
    suiteNegative = unittest.TestSuite()

    # Positive Tests
    suitePositive.addTest(testClass.ezmathTest("testDistance1"))
    suitePositive.addTest(testClass.ezmathTest("testDistanceZero"))
    suitePositive.addTest(testClass.ezmathTest("testAddPoints1"))
    suitePositive.addTest(testClass.ezmathTest("testAddPointsZero"))
    suitePositive.addTest(testClass.ezmathTest("testSubtractPoints1"))
    suitePositive.addTest(testClass.ezmathTest("testSubtractPointsZero"))
    suitePositive.addTest(testClass.ezmathTest("testMultPoint1"))
    suitePositive.addTest(testClass.ezmathTest("testMultPointZero"))
    suitePositive.addTest(testClass.ezmathTest("testxyComponent1"))
    suitePositive.addTest(testClass.ezmathTest("testxyComponentZero"))
    suitePositive.addTest(testClass.ezmathTest("testDirection1"))
    suitePositive.addTest(testClass.ezmathTest("testDirectionZero"))
    suitePositive.addTest(testClass.ezmathTest("testNormal1"))
    suitePositive.addTest(testClass.ezmathTest("testNormalZero"))
    suitePositive.addTest(testClass.ezmathTest("testRoundPointUp"))
    suitePositive.addTest(testClass.ezmathTest("testRoundPointDown"))
    suitePositive.addTest(testClass.ezmathTest("testRoundPointUpZero"))
    suitePositive.addTest(testClass.ezmathTest("testRoundPointDownZero"))
    #suitePositive.addTest(testClass.ezmathTest("testRandPoint"))

    # Negative Tests
    suiteNegative.addTest(testClass.ezmathTest("testDistanceNegative1"))
    suiteNegative.addTest(testClass.ezmathTest("testDistanceNegativeZero"))
    suiteNegative.addTest(testClass.ezmathTest("testDirectionNegative1"))
    suiteNegative.addTest(testClass.ezmathTest("testDirectionNegativeZero"))

    # Nest test suites
    suite = unittest.TestSuite((suitePositive, suiteNegative))

    # Return test suite to runner to execution
    return suite

# Test Case Main
if __name__ == '__main__':
    if '--unittest' in sys.argv:
        subprocess.call([sys.executable, '-m', 'unittest', 'discover'])

    runner = unittest.TextTestRunner()
    # Test Suite
    test_suite = suite()
    # Test Runner
    runner.run(test_suite)
