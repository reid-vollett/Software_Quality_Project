import unittest
import sys
import os
import subprocess

sys.path.append(os.path.abspath('..'))

from Classes import testClasses as testClass

# Test Suite
def suite():
    # Add test suites
    suiteClasses = unittest.TestSuite()

    suiteClasses.addTest(testClass.ezmathTest("testDistance"))
    suiteClasses.addTest(testClass.ezmathTest("testAddPoints"))
    suiteClasses.addTest(testClass.ezmathTest("testSubtractPoints"))
    suiteClasses.addTest(testClass.ezmathTest("testMultPoint"))
    suiteClasses.addTest(testClass.ezmathTest("testxyComponent"))
    suiteClasses.addTest(testClass.ezmathTest("testDirection"))
    suiteClasses.addTest(testClass.ezmathTest("testNormal"))
    suiteClasses.addTest(testClass.ezmathTest("testRoundPoint"))
    #suiteClasses.addTest(testClass.ezmathTest("testRandPoint"))

    # Nest test suites here
    suite = unittest.TestSuite((suiteClasses))

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
