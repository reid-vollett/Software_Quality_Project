import unittest
import sys
import os
import subprocess
import ezmath, gameFunctions

class ezmathTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDistance1(self):
        self.assertAlmostEqual(ezmath.distance((10,10)), 14.1421356237)

    def testDistanceZero(self):
        self.assertAlmostEqual(ezmath.distance((0,0)), 0)

    def testDistanceNegative1(self):
        self.assertNotAlmostEquals(ezmath.distance((10,10)), 28.1421356237)

    def testDistanceNegativeZero(self):
        self.assertNotAlmostEquals(ezmath.distance((0,0)), 1)

    def testAddPoints1(self):
        self.assertTupleEqual(ezmath.addPoints((10,10), (10,10)), (20,20))

    def testAddPointsZero(self):
        self.assertTupleEqual(ezmath.addPoints((0,0), (0,0)), (0,0))

    def testSubtractPoints1(self):
        self.assertTupleEqual(ezmath.subtractPoints((10, 10), (10, 10)), (0, 0))

    def testSubtractPointsZero(self):
        self.assertTupleEqual(ezmath.subtractPoints((0, 0), (0, 0)), (0, 0))

    def testMultPoint1(self):
        self.assertTupleEqual(ezmath.multPoint((10, 10), 2), (20, 20))

    def testMultPointZero(self):
        self.assertTupleEqual(ezmath.multPoint((0, 0), 0), (0, 0))

    def testxyComponent1(self):
        self.assertTupleEqual(ezmath.xyComponent(60), (-0.9524129804151563, -0.3048106211022167))

    def testxyComponentZero(self):
        self.assertTupleEqual(ezmath.xyComponent(0), (1, 0))

    def testDirection1(self):
        self.assertAlmostEqual(ezmath.direction((10,10)), 0.785398163)

    def testDirectionZero(self):
        self.assertAlmostEqual(ezmath.direction((0,0)), 0)

    def testDirectionNegative1(self):
        self.assertNotEqual(ezmath.direction((10,10)), 10.785398163)

    def testDirectionNegativeZero(self):
        self.assertNotEqual(ezmath.direction((0,0)), -1)

    def testNormal1(self):
        self.assertTupleEqual(ezmath.normal((10,10)), (-0.7071067811865475, -0.7071067811865476))

    def testNormalZero(self):
        self.assertTupleEqual(ezmath.normal((0,0)), (1,0))

    def testRoundPointUp(self):
        self.assertTupleEqual(ezmath.roundPoint((10.9, 10.9)), (11, 11)) # rounding up

    def testRoundPointDown(self):
        self.assertTupleEqual(ezmath.roundPoint((10.1, 10.1)), (10, 10))  # rounding down

    def testRoundPointUpZero(self):
        self.assertTupleEqual(ezmath.roundPoint((0, 0)), (0,0)) # rounding up

    def testRoundPointDownZero(self):
        self.assertTupleEqual(ezmath.roundPoint((0,0)), (0,0))  # rounding down

class gameFunctionsTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass