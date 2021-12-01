class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        
        for i in range(len(prefix)):
            p = prefix[:len(prefix) - i]
            items = [item for item in strs if item.startswith(p)]
            if len(items) == len(strs):
                return p
        return ""
