class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted=nums.sort()
        s=0
        n=len(nums)
        for i in range(0,n-1):
            if(nums[i]==nums[i+1]):
                s+=1
        if s==0:
            return False
        else:
            return True

            




        