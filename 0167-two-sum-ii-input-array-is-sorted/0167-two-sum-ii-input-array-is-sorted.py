class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # l=[]
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if(numbers[i]+numbers[j]==target):
        #             l.append(i+1)
        #             l.append(j+1)
        #             return l\
        right=0
        left=len(numbers)-1
        l=[]
        while right < left:
            if numbers[right]+numbers[left]>target:
                left=left-1
            if numbers[right]+numbers[left]<target:
                right=right+1
            if numbers[right]+numbers[left]==target:
                l.append(right+1)
                l.append(left+1)
                return l
        

            


        