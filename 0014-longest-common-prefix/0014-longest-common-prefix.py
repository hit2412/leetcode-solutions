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

        res = ""

        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i == len(s) or s[i] != strs[0][i]:
        #             return res
        #     res += strs[0][i]

        # return res
