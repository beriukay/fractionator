import re
from number import Number

def isNumber(number):
    if not number: 
        return False # For empty strings
    hasValidCharacters = bool(re.match("^[0-9_/-]*$", number))
    hasDigits = bool(re.search("\d+", number))
    hasValidFraction = True
    if '/' in number:
        hasValidFraction = bool(re.search("-?\d+\/-?\d+", number))
    return hasValidCharacters and hasDigits and hasValidFraction


def evaluate(tokenList):
    print(tokenList)
    result = Number("0") 
    for token in tokenList:
        if isNum(token):
            number = Number(token)
        pass
    return


def main():
    print("Fractionator (press q to quit)")
    while True:
        request = input("? ")
        if request in ['q', "quit"]:
            exit(0)
        elif "/0" in request or "/ 0" in request:   
            print("Sorry, I am not equipped to divide by zero.")
            continue
        sanitized = re.sub("[a-zA-Z!@#$%^&.,]",'', request)
        tokens = request.split(' ')
        tokens = [token for token in tokens if token != '']
        ignoreList = []
        for token in tokens:
            if not isNumber(token):
                ignoreList.append(token)
            else:
                break
        for ignore in ignoreList:
            tokens.remove(ignore)

        if len(tokens) < 3:             # if not enough to form an expression
            print('=',''.join([num for num in tokens if isNumber(num)]))
            continue
        evaluate(tokens)

#main()
good = ['1', '1/2', '1_1/2', '3_3/4', '5_0/5', '_2/3', '3_150/9', '-20/-4',
        '20', '2/3', '_2/3', '29_3/4', '1_45/3', '56_0/3', '1_-1/-1', '0', 
        '0_2/16', '-5_13/7']
numbers = [Number(i) for i in good]


bad = ['', 'a', '123.0', '12,3', 'helpme', '-_/-', '1_/2', '_/3', '-_-/']
#for i in bad:
#    print(i, isNumber(i))



test_cases = [
        ("1/2 * 3_3/4", "1_7/8"), 
        ("2_3/8 + 9/8", "3_1/2"),
        ("1", "1"),
        ("1/0", "div zero error"),
        ("-1 - -1/1", "0"),
        ("1 + 1/-1", "0"),
        ]

# Unhandled kinds of inputs: 2/3_, /3, /; Note: x/0 is handled in the main loop.
