class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # l=[]
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if(numbers[i]+numbers[j]==target):
        #             l.append(i+1)
        #             l.append(j+1)
        #             return l\
        right, left = 0, len(numbers)-1
        while right < left:
            if numbers[right]+numbers[left]>target:
                left=left-1
            elif numbers[right]+numbers[left]<target:
                right=right+1
            else:
                return [right+1, left+1]
        

            


        