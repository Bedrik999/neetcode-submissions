class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_1={}
        letters_2={}
        for i in s:
            if i in letters_1:
                letters_1[i]+=1
            else: 
                letters_1[i]=1
        for j in t: 
            if j in letters_2:
                letters_2[j]+=1
            else: 
                letters_2[j]=1
        if letters_1 == letters_2:
            return True
        else: 
            return False