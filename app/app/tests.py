"""

Test 
"""

from django.test import SimpleTestCase

from app import calc


class CalcClass(SimpleTestCase):
    def testaddFunction(self):
        res = calc.add(3,5)
        self.assertEqual(res, 8)

    def testSubtract(self):
        result = calc.subtract(4,54)
        self.assertEqual(result, 50)
