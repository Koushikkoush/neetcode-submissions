class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=s.lower()
        l=""
        for i in s1:
            if i.isalnum():
                l=l+i

        return l==l[::-1]