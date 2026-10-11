class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        all_num=1
        ind_zero=[]
        answer=[]
        for i in range(len(nums)):
            if nums[i]==0:
                ind_zero.append(i)
            else:
                all_num=all_num*nums[i]
        
        if len(ind_zero) == 1:
            answer+=[0]*len(nums)
            answer[ind_zero[0]]=all_num
        elif len(ind_zero) > 1:
            answer+=[0]*len(nums)
        else:
            for i in range(len(nums)):
                answer.append(int(all_num/nums[i]))
        return answer