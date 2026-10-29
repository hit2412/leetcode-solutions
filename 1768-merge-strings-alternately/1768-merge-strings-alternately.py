class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count = max( len(word1), len(word2))
        strj=[]
        for i in range(count):
            if( i < len(word1)):
                strj.append(word1[i])
            if (i < len(word2)):
                strj.append(word2[i])
        return "".join(strj)
            
