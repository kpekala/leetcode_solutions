class Solution:
    def letterCombinations(self, digits: str):
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if len(digits) == 1:
            return [digit for digit in dic[digits[0]]]
        if len(digits) == 0:
            return []
        combs = self.letterCombinations(digits[1:])
        res = []
        for comb in combs:
            for digit in dic[digits[0]]:
                res.append(digit + comb)
        return res

sol = Solution()

print(sol.letterCombinations("23"))
