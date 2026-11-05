class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # l=[]
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if(numbers[i]+numbers[j]==target):
        #             l.append(i+1)
        #             l.append(j+1)
        #             return l\
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left]+numbers[right]>target:
                right=right-1
            elif numbers[left]+numbers[right]<target:
                left=left+1
            else:
                return [left+1, right+1]
        

            


        