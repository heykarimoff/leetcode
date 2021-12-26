"""
Infix notation: (a+b)*c
Postfix notation: ab+c*
Prefix notation: *+abc

Given Q is a infix expression, evaluate the value of Q.
V is an empty value stack, and O is an empty operator stack.

While there are still tokens in Q:
    If the token is a number, push it onto V.
    If the token is a left parenthesis, push it onto O.
    If the token is a right parenthesis,
        While the operator at the top of O is not a left parenthesis,
            pop operators from O and values from V,
            apply the operator to the values, and push the result onto V.
        Pop the left parenthesis from O and discard it.
    If the token is an operator
        While O is not empty and the operator at the top of O has a higher or equal precedence to the operator in the token:
            Pop the operator from O and pop the corresponding values from V.
            Push the result onto V.
        Push the operator onto O.
While O is not empty:
    Pop the operator from O and pop the corresponding values from V.
    Push the result onto V.
Assume that the operator stack is empty at the end of the expression.
V contains the result of the expression.
"""


def apply(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a // b


def evaluate(tokens: str) -> int:
    V = []
    O = []
    for index, token in enumerate(tokens):
        print(f"token: {token}")
        if token == " ":
            continue
        elif token.isdigit():
            print(f"token is digit: {token.isdigit()}")
            if (
                not V
                and tokens[index - 1] == "-"
                or (
                    index >= 2
                    and tokens[index - 2] == "("
                    and tokens[index - 1] == "-"
                )
            ):
                print(f"token is negative: {tokens[index - 1] == '-'}")
                V.append(-int(token))
                O.pop()
            elif V and tokens[index - 1].isdigit():
                print(f"prev token is digit: {tokens[index - 1].isdigit()}")
                V[-1] = V[-1] * 10 + int(token)
            else:
                V.append(int(token))
        elif token == "(":
            print(f"token is left paranthesis")
            O.append(token)
        elif token == ")":
            print(f"token is right paranthesis")
            while O and O[-1] != "(":
                b, a = V.pop(), V.pop()
                V.append(apply(a, b, O.pop()))
            O.pop()
        elif token in "+-*/":
            while (
                O
                and len(V) >= 2
                and (
                    (token in "+-" and O[-1] in "+-")
                    or (token in "*/" and O[-1] in "*/")
                    or (token in "+-" and O[-1] in "*/")
                )
            ):
                b, a = V.pop(), V.pop()
                V.append(apply(a, b, O.pop()))
            O.append(token)
        print(f"O: {O}")
        print(f"V: {V}")
    print(f"O: {O}")
    print(f"V: {V}")
    while O and len(V) >= 2:
        b, a = V.pop(), V.pop()
        V.append(apply(a, b, O.pop()))

    if len(O) == 1 and O[-1] == "-" and len(V) == 1:
        print(f"len(O) == 1 and O[-1] == '-' and len(V) == 1")
        return f"-{V[0]}"
    return "".join([str(i) for i in V])


def test_evaluate():
    assert evaluate("1+2*3") == "7"
    assert evaluate(" 3 / 2") == "1"
    assert evaluate(" 42") == "42"
    assert evaluate("0-2147483647") == "-2147483647"
    assert evaluate("1-1+1") == "1"


def test_evaluate_with_paranthesis():
    assert evaluate("1 + 1") == "2"
    assert evaluate(" 2 - 1 + 2 ") == "3"
    assert evaluate("-2+ 1") == "-1"
    assert evaluate("- (3 + (4 + 5))") == "-12"
    assert evaluate("1-(-2)") == "3"
    assert evaluate("-(3+4)+5") == "-2"
    assert evaluate("(1+(4+5+2)-3)+(6+8)") == "23"
    assert evaluate("(1*(4+5+2)-3)/(6+2)") == "1"
