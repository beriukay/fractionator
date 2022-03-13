# Number takes a string input of integer, mixed, or fractional values. It does
# not sanitize inputs. The class handles all mathematical operations on its data.
class Number:
    def __init__(self, number, numerator=None, denominator=None, sign=None):
        if type(number) is str:
            whole, num, denom = self.splitValue(number)
            self.sign = self.handleSign(whole, num, denom)
            whole, num, denom = abs(whole), abs(num), abs(denom)
            self.whole, self.num, self.den = self.reduce(whole, num, denom)
            if self.whole < 0:
                self.whole, self.num = self.balanceNegatives()
        else:
            self.whole = number
            self. num = numerator
            self.den = denominator
            self.sign = sign

    def reduce(self, whole, num, denom):
        gcd = self.getGCD(num, denom)
        num = int(num / gcd)
        denom = int(denom / gcd)
        if num >= denom:                    # Check for improper fraction
            whole += int(num / denom)       # Carry over whole values
            num = num % denom
        return whole, num, denom

    def getGCD(self, first, second):
        if (first < second):
            return self.getGCD(second, first)
        if first == 0:
            return second
        elif second == 0:
            return first
        return self.getGCD(second, first % second)

    def splitValue(self, numStr):
        whole, num, denom = 0, 0, 1
        if '_' in numStr:                   # Split whole part from fractional
            wholePart, numStr = numStr.split('_')
            if wholePart:
                whole = int(wholePart)
        if '/' in numStr:                   # Split fraction into components
            num, denom = numStr.split('/')
            num, denom = int(num), int(denom)
        else:                               # Handle solo integers
            whole = int(numStr)
        return whole, num, denom
    
    # Multiply values together to set the +/- parity, then scale to range [-1,1]
    def handleSign(self, a, b, c):
        return 2 * int(a * b * c >= 0) - 1

    def balanceNegatives(self, number=None):
        if number is None:
            number = self
        whole = number.whole
        num, den = number.num, number.den
        if num > 0:
            whole += 1
            num = den - self.num
        return whole, num
    
    def __add__(self, other):
        whole, num, den, sign = 0, 0, 0, self.sign
        if self.sign == other.sign:
            top = self.num * other.den + other.num * self.den
            whole, num, den = self.reduce(self.whole + other.whole, top, self.den * other.den)
        else:
            improperSelf = self.whole * self.den + self.num 
            improperOther =  other.whole * other.den + other.num
            top = improperSelf * other.den - improperOther * self.den
            print("top: ", top)
            whole, num, den = self.reduce(self.whole - other.whole, top, self.den * other.den)
            print(whole, num, den)
            result = Number(whole, num, den, sign)
            result.whole, result.num = result.balanceNegatives()
        return result

    def __sub__(self, other):
        negOther = Number(other.whole, other.num, other.den, -1 * other.sign)
        return self + negOther

    def __repr__(self):
        repStr = ''
        if self.whole != 0:
            repStr += str(self.whole) + '_'
        if self.num != 0:
            repStr += str(self.num) + '/' + str(self.den)
        if self.whole == 0 and self.num == 0:
            repStr = "0"
        return repStr
