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
    suitePositive.addTest(testClass.ezmathTest("testDistance"))
    suitePositive.addTest(testClass.ezmathTest("testAddPoints"))
    suitePositive.addTest(testClass.ezmathTest("testSubtractPoints"))
    suitePositive.addTest(testClass.ezmathTest("testMultPoint"))
    suitePositive.addTest(testClass.ezmathTest("testxyComponent"))
    suitePositive.addTest(testClass.ezmathTest("testDirection"))
    suitePositive.addTest(testClass.ezmathTest("testNormal"))
    suitePositive.addTest(testClass.ezmathTest("testRoundPoint"))
    #suitePositive.addTest(testClass.ezmathTest("testRandPoint"))

    # Negative Tests
    suiteNegative.addTest(testClass.ezmathTest("testDistanceNegative"))
    suiteNegative.addTest(testClass.ezmathTest("testDirectionNegative"))

    # Nest test suites
    suite = unittest.TestSuite((suitePositive, suiteNegative))

    # Return test suite to runner to execution
    return suite

# Test Case Main
if __name__ == '__main__':
    # Usage in PyCharm is normal, to run from command line add --unittest at end
    if '--unittest' in sys.argv:
        subprocess.call([sys.executable, '-m', 'unittest', 'discover'])

    runner = unittest.TextTestRunner()
    # Test Suite
    test_suite = suite()
    # Test Runner
    runner.run(test_suite)
