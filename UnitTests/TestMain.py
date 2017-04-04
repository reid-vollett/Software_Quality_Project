import unittest
import sys
import os
import subprocess

sys.path.append(os.path.abspath('..'))

from Classes import testClasses as testClass

# Test Suite
def suite():
    # Add test suites here
    suiteGeneral = unittest.TestSuite()
    suiteClasses = unittest.TestSuite()
    suiteFunctions = unittest.TestSuite()

    # Add test cases to suiteGeneral here

    # Add test cases to suiteClasses here
    suiteClasses.addTest(testClass.BasherTest("testCase"))
    suiteClasses.addTest(testClass.AlienTest("testCase"))

    # Add test cases to suiteFunctions here

    # Nest test suites here
    suite = unittest.TestSuite((suiteGeneral, suiteClasses))

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
