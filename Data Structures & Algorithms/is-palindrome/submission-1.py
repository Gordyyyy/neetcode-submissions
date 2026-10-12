class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""

        for char in s.lower():
            if char.isalnum():
                newS += char

        return newS == newS[::-1]
