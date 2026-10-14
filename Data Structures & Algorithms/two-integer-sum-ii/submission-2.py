class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ln_mas=len(numbers)
        i=0
        j=ln_mas-1
        while i<=ln_mas and j>=0:
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j]<=target:
                i+=1
            else:
                j-=1
        return "Nothing"