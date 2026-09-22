class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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

    


        
        

        