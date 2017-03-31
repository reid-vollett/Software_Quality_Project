from unittest import TestCase
import Conversions


class ConversionTesting(TestCase):
    def test_DecToBinZero(self):
        self.assertEqual(Conversions.ConvertDecToBin.DecToBin(0), 0)

    def test_DecToDinOne(self):
        self.assertEqual(Conversions.ConvertDecToBin.DecToBin(1), 1)

    def test_DecToBin42(self):
        self.assertEqual(Conversions.ConvertDecToBin.DecToBin(42), 101010)

    def test_DecToBinLarge(self):
        self.assertEqual(Conversions.ConvertDecToBin.DecToBin(512), 1000000000)

    def test_BinToDecZero(self):
        self.assertEqual(Conversions.ConvertBinToDec.BinToDec(0), 0)

    def test_BinToDecOne(self):
        self.assertEqual(Conversions.ConvertBinToDec.BinToDec(1), 1)

    def test_BinToDec42(self):
        self.assertEqual(Conversions.ConvertBinToDec.BinToDec(101010), 42)

    def test_BinToDecLarge(self):
        self.assertEqual(Conversions.ConvertBinToDec.BinToDec(1000000000), 512)






