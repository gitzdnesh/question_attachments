import unittest
from unit_converter import convert_units

class UnitConverterTest(unittest.TestCase):
    def testPoundToKg(self):
        self.assertEqual(2.25, round(convert_units(5, "pound", 0.45), 2))

    def testMilesToKm(self):
        self.assertEqual(141.53, round(convert_units(87.9, "mile", 1.61), 2))

if name == "main":
    unittest.main()