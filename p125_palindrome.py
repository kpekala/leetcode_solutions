class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for c in s:
            if (ord(c) <= 122 and ord(c) >= 97) or (ord(c) >= 48 and ord(c) <= 57) or (ord(c) <= 90 and ord(c) >= 65):
                if ord(c) < 97 and ord(c) >= 65:
                    c = chr(ord(c) + 32)
                new_s += c
        print(new_s[::-1], new_s)
        return new_s[::-1] == new_s


print(Solution().isPalindrome("bab"))