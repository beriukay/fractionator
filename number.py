# Number takes a string input of integer, mixed, or fractional values. It does
# not sanitize inputs. The class handles all mathematical operations on its data.
# Class constructor is overloaded to take valid string or processed Number input.
class Number:
    def __init__(self, number, denominator=None):
        if type(number) is str:
            whole, num, den = self.splitValue(number)
            whole, num, self.den = int(whole), int(num), int(den)
            self.num = self.makeImproper(whole, num, den)
        else:
            self. num = number
            self.den = denominator

    def splitValue(self, numStr):
        whole, num, den = 0, 0, 1
        if '_' in numStr:                   # Split whole part from fractional
            wholePart, numStr = numStr.split('_')
            if wholePart:
                whole = int(wholePart)
        if '/' in numStr:                   # Split fraction into components
            num, den = numStr.split('/')
            num, den = int(num), int(den)
        else:                               # Handle solo integers
            whole = int(numStr)
        return whole, num, den

    def getGCD(self, first, second):        # GCD is used to reduce fractions
        if (first < second):
            return self.getGCD(second, first)
        if first == 0:
            return second
        elif second == 0:
            return first
        return self.getGCD(second, first % second)

    # Improper fractions are either a + b/c or -a - b/c. In other words,
    # the numerator and whole components always have the same sign.
    def makeImproper(self, whole, num, den):
        return (whole * den) + num if whole >=0 else (whole * den) - num

    def makeMixed(self, num=None, den=None):
        if not num or not den:
            num, den = self.num, self.den
        whole = 0
        gcd = self.getGCD(abs(num), abs(den))
        num, den = int(num / gcd), int(den / gcd)
        if abs(num) >= abs(den):            # Reduce and carry
            whole = int(num / den)
            num = abs(num) % den
        return whole, num, den

    def __add__(self, other):               # a/b + c/d = (ad + cb)/ad
        newNum = self.num * other.den + other.num * self.den
        return Number(newNum, self.den * other.den)

    def __sub__(self, other):
        return self +  Number(-1 * other.num, other.den)

    def __mul__(self, other):               # a/b * c/d = ac / bd
        return Number(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        return self * Number(other.den, other.num)

    def __repr__(self):
        repStr = ''
        if self.num == 0:
            repStr = "0"
        else:
            whole, num, den = self.makeMixed()
            if whole != 0:
                repStr += str(whole) + "_"
            repStr += str(num) + '/' + str(den)
        return repStr
