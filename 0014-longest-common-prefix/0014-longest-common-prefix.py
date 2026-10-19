class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest_str = min(len(w) for w in strs)   
        prefix = ""                            

        for pos in range(shortest_str):           
            letter = strs[0][pos]              
            for j in range(1, len(strs)):      
                if strs[j][pos] != letter:     
                    return prefix              
            prefix += letter                   
        return prefix                          
        