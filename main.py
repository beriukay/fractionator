import re

# Possible kinds of input: 20, 2/3, _2/3, 29_3/4, 1_45/3, 1_0/3, -1/-1
# Unhandled kinds of inputs: 2/3_, /3, /; Note: x/0 is handled in the main loop.
class Number:
    def __init__(self, number):
        self.whole, num, denom = self.splitValue(number)
        carry, self.fraction = self.reduce(num, denom)
        self.whole += carry
        self.balanceNegatives()

    def reduce(self, num, denom):
        carry = 0
        gcd = self.getGCD(num, denom)
        num = int(num / gcd)
        denom = int(denom / gcd)
        if num >= denom: # Check for improper fraction
            carry = int(num / denom)
            num = num % denom
        return carry, (num, denom)

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
        if '_' in numStr:
            wholePart, numStr = numStr.split('_')
            if wholePart:
                whole = int(wholePart)

        if '/' in numStr:
            num, denom = numStr.split('/')
            if num is not None and denom is not None:
                num, denom = int(num), int(denom)
            if num < 0 and denom < 0:
                num, denom = -1 * num, -1 * denom
        else:
            whole = int(numStr)
            num, denom = 0, 1
        return whole, num, denom
    
    def balanceNegatives(self):
        if self.whole < 0:
            if self.fraction[0] > 0:
                self.whole += 1
                newNum = self.fraction[1] - self.fraction[0]
                self.fraction = (newNum, self.fraction[1])


def evaluate(tokenList):
    print(tokenList)
    for token in tokenList:
        pass
    return


def main():
    print("Fractionator (press q to quit)")
    operators = {' + ':" add ", ' - ':" add ", ' * ':" mul ", " / ": " mul ", '(':"left", 
            ')':"right"}
    while True:
        request = input("? ")
        if request in ['q', "quit"]:
            exit(0)
        # Fall through if any zero division is detected.
        elif "/0" in request or "/ 0" in request:
            print("Sorry, I am not equipped to divide by zero.")
        elif re.match("[^0-9_+\-*/]", request):
            print("Sorry, I do not recognize some of the characters provided")
        else:
            for operator in operators:
                request = request.replace(operator, operators[operator])

            tokens = request.split(' ')
            evaluate(tokens)


#main()
testNums = ['1', '1/2', '1_1/2', '3_3/4', '5_0/5', '_2/3', '3_150/9', '-20/-4',
        '20', '2/3', '_2/3', '29_3/4', '1_45/3', '56_0/3', '1_-1/-1', '0', 
        '0_2/16', '-5_13/7']
numbers = [Number(i) for i in testNums]

test_cases = [
        ("1/2 * 3_3/4", "1_7/8"), 
        ("2_3/8 + 9/8", "3_1/2"),
        ("1", "1"),
        ("1/0", "div zero error"),
        ("-1 - -1/1", "0"),
        ("1 + 1/-1", "0"),
        ]

