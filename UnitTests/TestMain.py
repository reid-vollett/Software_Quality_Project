import unittest
import sys
import subprocess

from Classes import testClasses as testClass

# Test Suite
def suite():
    suiteGeneral = unittest.TestSuite()
    suiteClasses = unittest.TestSuite()

    suiteClasses.addTest(testClass.Basher("setUp"))
    suiteGeneral.addTest(testClass.Alien("testCase"))

    suite = unittest.TestSuite((suiteGeneral, suiteClasses))

    return suite

# Main
if __name__ == '__main__':
    # Usage in PyCharm is normal, to run from command line add --unittest at end
    if '--unittest' in sys.argv:
        subprocess.call([sys.executable, '-m', 'unittest', 'discover'])

    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
