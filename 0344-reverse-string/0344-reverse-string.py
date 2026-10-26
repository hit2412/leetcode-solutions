class Solution:
    def reverseString(self, s: list[str]) -> None:
        right = len(s) - 1
        for left in range(len(s) // 2):
            s[left], s[right - left] = s[right - left], s[left]
            # t=s[i]
            # s[i]=s[n-i]
            # s[n-i]=t
