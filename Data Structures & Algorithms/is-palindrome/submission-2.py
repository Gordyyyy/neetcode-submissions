class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Set up two pointers
        leftPointer = 0
        rightPointer = len(s) -1

        while leftPointer < rightPointer:
            if not s[leftPointer].isalnum():
                leftPointer += 1
                continue
            if not s[rightPointer].isalnum():
                rightPointer -= 1
                continue
            if s[leftPointer].lower() != s[rightPointer].lower():
                return False
                
            leftPointer += 1
            rightPointer -= 1
        return True
            
        