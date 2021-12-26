# https://leetcode.com/problems/basic-calculator-ii/

# Time: O(n)
# Space: O(n)


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
                    b, a = V.pop(), V.pop()
                    V.append(self.apply(a, b, O.pop()))
                O.append(token)

        while O:
            b, a = V.pop(), V.pop()
            V.append(self.apply(a, b, O.pop()))
        return "".join([str(i) for i in V])

    def apply(self, a, b, operator):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return a // b
