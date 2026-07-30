class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        largest=0
        length=0
        current=0
        for i in num_set:
            if i-1 in num_set:
                continue
            else:
                length=1
                current=i
            while current+1 in num_set:
                length+=1
                current+=1
            if largest<length:
                    largest=length
        return largest
            



        