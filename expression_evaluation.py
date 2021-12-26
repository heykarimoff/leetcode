"""
Infix notation: (a+b)*c
Postfix notation: ab+c*
Prefix notation: *+abc

Given Q is a infix expression, evaluate the value of Q.
V is an empty value stack, and O is an empty operator stack.

While there are still tokens in Q:
    If the token is a number, push it onto V.
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


def evaluate(tokens: str) -> int:
    V = []
    O = []
    for index, token in enumerate(tokens):
        if token == " ":
            continue
        elif token.isdigit():
            if V and tokens[index - 1].isdigit():
                V[-1] = V[-1] * 10 + int(token)
            else:
                V.append(int(token))
        elif token in "+-*/":
            while O and (
                (token in "+-" and O[-1] in "+-")
                or (token in "*/" and O[-1] in "*/")
                or (token in "+-" and O[-1] in "*/")
            ):
                o = O.pop()
                b, a = V.pop(), V.pop()
                if o == "+":
                    V.append(a + b)
                elif o == "-":
                    V.append(a - b)
                elif o == "*":
                    V.append(a * b)
                elif o == "/":
                    V.append(a // b)
            O.append(token)

    while O:
        o = O.pop()
        b, a = V.pop(), V.pop()

        if o == "+":
            V.append(a + b)
        elif o == "-":
            V.append(a - b)
        elif o == "*":
            V.append(a * b)
        elif o == "/":
            V.append(a // b)

    return "".join([str(i) for i in V])


if __name__ == "__main__":
    # print(evaluate("1+2*3"))
    # print(evaluate(" 3 / 2"))
    # print(evaluate(" 42"))
    # print(evaluate("0-2147483647"))
    print(evaluate("1-1+1"))
