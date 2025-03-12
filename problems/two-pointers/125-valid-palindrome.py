class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalnum(c: str) -> bool:
            return (
                ('a' <= c <= 'z') or
                ('A' <= c <= 'Z') or
                ('0' <= c <= '9')
            )


        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not isalnum(s[left]): 
                left += 1
            while left < right and not isalnum(s[right]):
                right -= 1
            
            if left < right and s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
        
