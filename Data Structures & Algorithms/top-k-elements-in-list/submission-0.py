class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        pairs=[]
        for i in freq:
            pairs.append((freq[i],i))
        pairs.sort(reverse=True)
        result=[]
        i=0
        while k!=0:
            result.append(pairs[i][1])
            i+=1
            k-=1
        return result