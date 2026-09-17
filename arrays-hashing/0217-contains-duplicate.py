class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
    # Approach 1: Brute force
    # Time: O(n^2) and Space: O(1)
    # Result: TLE (too slow for n up to 10^5)

        # n=len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]==nums[j]:
        #             return True
        # return False

    # Approach 2: Hash set
    # Time: O(n) and Space: O(n)

        check = set()
        for num in nums:
            if num in check:
                return True
            check.add(num)
        return False

        
