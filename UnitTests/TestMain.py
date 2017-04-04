import unittest
import sys
import subprocess


class Alien(unittest.TestCase):
    pass


class Asteroird(unittest.TestCase):
    pass


class Basher(unittest.TestCase):
    pass


class Camera(unittest.TestCase):
    pass


class Circ(unittest.TestCase):
    pass


class DeflectorShield(unittest.TestCase):
    pass


class Enemy(unittest.TestCase):
    pass


class EnemyBullet(unittest.TestCase):
    pass


# Should be a good place to put alot of unit tests
class ezmath(unittest.TestCase):
    pass


class gameFunctions(unittest.TestCase):
    pass


class GlobalVariables(unittest.TestCase):
    pass


# cant really do anything here
class Img(unittest.TestCase):
    pass


class IonBullet(unittest.TestCase):
    pass


class IonCannon(unittest.TestCase):
    pass


class Item(unittest.TestCase):
    pass


class Missile(unittest.TestCase):
    pass


class MissileLauncher(unittest.TestCase):
    pass


class MotherCow(unittest.TestCase):
    pass


class MotherCowDeath(unittest.TestCase):
    pass


class OverShield(unittest.TestCase):
    pass


class Particle(unittest.TestCase):
    pass


class Player(unittest.TestCase):
    pass


class Poly(unittest.TestCase):
    pass


class Projectile(unittest.TestCase):
    pass


class QuadShooter(unittest.TestCase):
    pass


class RapidGun(unittest.TestCase):
    pass


class Shaper(unittest.TestCase):
    pass


class SpaceGame(unittest.TestCase):
    pass


class SpreadGun(unittest.TestCase):
    pass


class Weapon(unittest.TestCase):
    pass


class ParticleSuper(unittest.TestCase):
    def setUp(self):
        print("Setup\n")
        #self.X = X

    def tearDown(self):
        print("Takedown\n")
        #self.X.dispose()

    def testCase(self):
        print("I am a test case, big and stronk1")

class EnemySuper(unittest.TestCase):
    def setUp(self):
        print("Setup\n")
        #self.X = X

    def tearDown(self):
        print("Takedown\n")
        #self.X.dispose()

    def testCase(self):
        print("I am a test case, big and stronk2")

# class ParticleTestPositive(ParticleSuper):
#    def runTest(self):
#        print("Start test\n")
#        #XXXXXXX

# Test Suite
def suite():
    suiteGeneral = unittest.TestSuite()
    suiteClasses = unittest.TestSuite()

    suiteClasses.addTest(ParticleSuper("testCase"))
    suiteGeneral.addTest(EnemySuper("testCase"))

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
