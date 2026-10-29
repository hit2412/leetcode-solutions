class Solution:
    def validPalindrome(self, s: str) -> bool:

        left, right = 0, len(s)-1
        while left < right:

            if ( s[left]!=s[right]):
                return self.helper(s,left+1,right) or self.helper(s,left,right-1)
            left=left+1
            right=right-1
        return True
    def helper(self,s,left,right):
        while left < right:

            if(s[left] != s[right]):
                return False
            left=left+1
            right=right-1
        return True