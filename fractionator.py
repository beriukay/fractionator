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


def tokenGenerator(iterable):
    iterator = iter(iterable)
    prev = None
    current = next(iterator) 
    for post in iterator:
        yield(prev, current, post)
        prev = current
        current = post
    yield(prev, current, None)


def tokenizeInput(text):
    sanitized = re.sub("[a-zA-Z!@#$%^&.,]",'', text)
    tokens = text.split(' ')
    tokens = [token for token in tokens if token != '']
    ignoreList = []
    for token in tokens:                # Ignore tokens until first digit
        if not isNumber(token):
            ignoreList.append(token)
        else:
            break
    for ignore in ignoreList:
        tokens.remove(ignore)
    if len(tokens) < 3:             # Too few inputs, return numbers in text
        print('=',''.join([num for num in tokens if isNumber(num)]))
        return None
    return tokens


# All valid inputs alternate operands and operators, starting with operands.
def evaluate(tokens):
    ops = "*/+-"
    tokenIter = tokenGenerator(tokens)
    for prev, this, post  in tokenIter:
        for op in ops:                  # Set order of operations
            if this == op and op == '*':
                accumulator = Number(prev) * Number(post)
            elif this == op and op == '/':
                accumulator = Number(prev) / Number(post)
            elif this == op and op == '+':
                accumulator = Number(prev) + Number(post)
            elif this == op and op == '-':
                accumulator = Number(prev) - Number(post)
            else:
                continue
            tokens.remove(prev)
            tokens.remove(this)
            post = accumulator
    return accumulator


def main():
    print("Fractionator (press q to quit)")
    while True:
        request = input("? ")
        if request in ['q', "quit"]:
            exit(0)
        elif "/0" in request or "/ 0" in request:   
            print("Sorry, I am not equipped to divide by zero.")
            continue
        tokens = tokenizeInput(request)
        if tokens == None:
            print()
            continue
        result = evaluate(tokens)
        print("=", result)
        print()
main()
