# https://leetcode.com/problems/basic-calculator-ii/


class Solution:
    def calculate(self, tokens: str) -> int:
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
                    token in "+-" or (token in "*/" and O[-1] in "*/")
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
