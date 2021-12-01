class BruteForceSolution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        str_x = str(x)
        length = len(str_x)
        for i in range(length // 2):
            if str_x[i] != str_x[length - i - 1]:
                return False
        return True

class ListReverseSolution:
    def isPalindrome(self, x: int) -> bool:
        # check if string x is the same as reversed string x
        str_x = str(x)
        return str_x == str_x[::-1]