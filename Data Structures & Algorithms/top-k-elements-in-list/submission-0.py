class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cn={}
        answer=[]
        for i in range(len(nums)):
            if nums[i] in cn:
                cn[nums[i]]+=1
            else:
                cn[nums[i]]=1
        cn=sorted(cn.items(), key=lambda item: item[1], reverse=True)
        for j in range(k):
            answer.append(cn[j][0])
        return answer
