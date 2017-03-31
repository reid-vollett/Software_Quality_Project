import unittest
import sys
import subprocess

# class ParticleSuper (unittest.Testcase):
#   def setUp(self):
#       print("Setup\n")
#   def tearDown(self):
#       print("Takedown\n")

# class ParticleTestPositive(ParticleSuper):
#   def runTest(self):
#       print("Start test\n")
#       XXXXXXX

# class ParticleTestFailure(ParticleSuper):
#   def runTest(self):
#       print("Start test\n")
#       XXXXXXX


def suite():
    suite = unittest.TestSuite()
    #suite.addTest(ParticleTestPositive)
    #suite.addTest(ParticleTestFailure)
    return suite

if __name__ == '__main__':
    if '--unittest' in sys.argv:
        subprocess.call([sys.executable, '-m', 'unittest', 'discover'])

    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)

