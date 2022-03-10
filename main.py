test_cases = [
        ("1/2 * 3_3/4", "1_7/8"), 
        ("2_3/8 + 9/8", "3_1/2"),
        ("1", "1"),
        ("1/0", "div zero error"),
        ("-1 - -1/1", "0"),
        ("1 + 1/-1", "0")
        ]


def main():
    print("Fractionator (press q to quit)")
    tokens = {'+':"add", '-':"add", '*':"mul", "/": "mul", '(':"left", 
            ')':"right"}
    while True:
        request = input("? ")
        if request == 'q':
            exit(0)
        # Fall through if any zero division is detected.
        elif "/0" in request or "/ 0" in request:
            print("Sorry, I am not equipped to divide by zero.")
        else:
            chunks = request.split(' ')
            print(chunks)


main()
