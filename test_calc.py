#Arihant Kuba
#June 16, 2021
#Idea for project taken from: https://www.youtube.com/watch?v=6tNS--WetLI

import unittest
from unittest.mock import patch
import calc

class TestCalc(unittest.TestCase):

    #general test without mocking
    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result, 15)

    # What happens when you dont use mocking
    #def test_dice_add(self):
    #    result = calc.dice_add(1)
    #    self.assertEqual(result, 2)

    #mocking with patch as a context manager
    #def test_dice_add(self):
    #    with patch('calc.d_roll.roll_dice') as mocked_roll:
    #        mocked_roll.return_value = 1
    #        result = calc.dice_add(1)
    #        self.assertEqual(result, 2)

    #mocking with patch as a decorator 
    @patch('calc.d_roll.roll_dice')
    def test_dice_add(self, mocked_roll):
        mocked_roll.return_value = 1
        result = calc.dice_add(1)
        self.assertEqual(result, 2)


if __name__ == '__main__':
        unittest.main()
