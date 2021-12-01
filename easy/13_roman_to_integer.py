# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        return sum(self.to_integer(s))

    def to_integer(self, romans: str) -> int:
        roman_to_integer = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        for index, numeral in enumerate(romans):
            if index > 0:
                previous_numeral = romans[index - 1]
                if roman_to_integer[previous_numeral] < roman_to_integer[numeral]:
                    yield roman_to_integer[numeral] - 2 * roman_to_integer[previous_numeral]
                    continue
            yield roman_to_integer[numeral]
        