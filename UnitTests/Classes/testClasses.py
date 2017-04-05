import unittest
import sys
import os
import subprocess
import Alien, Asteroid, Basher, Camera, Circ, DeflectorShield, Enemy, EnemyBullet, ezmath, gameFunctions, \
    GlobalVariables, IonBullet, IonCannon, Item, Missile, MissileLauncher, MotherCow, MotherCowDeath, OverShield, \
    Particle, Player, Poly, Projectile, QuadShooter, RapidGun, Shape, SpreadGun, Weapon

class ezmathTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDistance(self):
        self.assertAlmostEqual(ezmath.distance((10,10)), 14.1421356237)

    def testAddPoints(self):
        self.assertTupleEqual(ezmath.addPoints((10,10), (10,10)), (20,20))

    def testSubtractPoints(self):
        self.assertTupleEqual(ezmath.subtractPoints((10, 10), (10, 10)), (0, 0))

    def testMultPoint(self):
        self.assertTupleEqual(ezmath.multPoint((10, 10), 2), (20, 20))

    def testxyComponent(self):
        self.assertTupleEqual(ezmath.xyComponent(60), (-0.9524129804151563, -0.3048106211022167))

    def testDirection(self):
        self.assertAlmostEqual(ezmath.direction((10,10)), 0.785398163)

    def testNormal(self):
        self.assertTupleEqual(ezmath.normal((10,10)), (-0.7071067811865475, -0.7071067811865476))

    def testRoundPoint(self):
        self.assertTupleEqual(ezmath.roundPoint((10.1, 10.1)), (10, 10)) # rounding down
        self.assertTupleEqual(ezmath.roundPoint((10.9, 10.9)), (11, 11)) # rounding up


class gameFunctionsTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass