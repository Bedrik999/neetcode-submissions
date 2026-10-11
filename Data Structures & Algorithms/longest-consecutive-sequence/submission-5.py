class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        else:
            nums.sort()
            mx_seq=1
            cnt=1
            for i in range(len(nums)-1):
                if nums[i+1]-nums[i]==1:
                    cnt+=1
                elif nums[i+1]-nums[i]==0:
                    continue
                else:
                    if mx_seq<cnt:
                        mx_seq=cnt
                        cnt=1
                    else:
                        cnt=1
            if mx_seq<cnt:
                mx_seq=cnt
            return mx_seq