class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = [0] * 26 
        count_t = [0] * 26

        for ch in s:
            count_s[ord(ch) - ord('a')] += 1

        for ch in t:
            count_t[ord(ch) - ord('a')] += 1

        return count_s == count_t


    
    # Time	O(n log n)and Space : O(n)
        return sorted(s)==sorted(t)
    #Brute force : Time: O(n^2) and Space: O(n)
        # if len(s)!=len(t):
        #     return False
        # lists=list(s)

        # for ch in t:
        #     if ch in lists:
        #         lists.remove(ch)
        #     else:
        #         return False
        # return True

    


        
        

        