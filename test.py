import fractionator
from fractions import Fraction as f
from number import Number
import unittest

good_input = ['1', '1/2', '1_1/2', '3_3/4', '5_0/5', '_2/3', '3_150/9', '-20/-4',
        '20', '2/3', '_2/3', '29_3/4', '1_45/3', '56_0/3', '1_-1/-1', '0', 
        '0_2/16', '-5_13/7']

good_number = ['1', '1/2', '3/2', '15/4', '5', '2/3', '59/3', '5',
        '20', '2/3', '2/3', '119/4', '48/3', '56', '2', '0', '1/8', '-48/7']
bad_input = ['', 'a', '123.0', '12,3', 'helpme', '-_/-', '1_/2', '_/3', '-_-/']
test_cases = [
        ("1/2 * 3_3/4", "1_7/8"), 
        ("2_3/8 + 9/8", "3_1/2"),
        ("-1 - -1/1", "0"),
        ("1 + 1/-1", "0"),
        ]

class TestNumber(unittest.TestCase):
    def test_good_input(self):
        for index in range(len(good_input)):
            testNumber = Number(good_input[index])
            num, den = testNumber.num, testNumber.den
            module_num = f(good_number[index])
            mNum, mDen = module_num.numerator, module_num.denominator
            self.assertEqual(str(num), str(mNum))
            self.assertEqual(str(den), str(mDen))

    def test_bad_input(self):
        for bad in bad_input:
            with self.assertRaises(ValueError):
               testNumber = Number(bad)

    def test_operations(self):
        for case in test_cases:
            expression, result = case[0], case[1]
            test_tokens = fractionator.tokenizeInput(expression)
            print(test_tokens)
            test_answer = fractionator.evaluate(test_tokens)
            self.assertEqual(str(test_answer), case[1])

if __name__ == '__main__':
    unittest.main(argv=['ignore'], exit=False)

