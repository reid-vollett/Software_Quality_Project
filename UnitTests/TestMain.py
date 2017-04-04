import unittest
import sys
import subprocess


class ParticleSuper(unittest.TestCase):
    def setUp(self):
        print("Setup\n")

    def tearDown(self):
        print("Takedown\n")

    def testCase(self):
        print("I am a test case, big and stronk")


# class ParticleTestPositive(ParticleSuper):
#    def runTest(self):
#        print("Start test\n")
#        #XXXXXXX

def suite():
    suite = unittest.TestSuite()
    suite.addTest(ParticleSuper("setUp"))
    return suite


if __name__ == '__main__':
    # Usage in PyCharm is normal, to run from command line add --unittest at end
    if '--unittest' in sys.argv:
        subprocess.call([sys.executable, '-m', 'unittest', 'discover'])

    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
