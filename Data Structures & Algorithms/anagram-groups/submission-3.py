class Solution:
    def isAnagram(self, s: str) -> dict:
        letters_1={}
        for i in s:
            if i in letters_1:
                letters_1[i]+=1
            else: 
                letters_1[i]=1
        return tuple(sorted(letters_1.items()))
        
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:   
        anograms=[]
        pred_final_answer={}
        final_answer=[]
        for i in range(len(strs)):
            anograms.append(self.isAnagram(strs[i]))
        for i in range(len(strs)):
            if anograms[i] not in pred_final_answer:
                pred_final_answer[anograms[i]]=[strs[i]]
            else:
                pred_final_answer[anograms[i]].append(strs[i])
        for i in pred_final_answer:
            final_answer.append(pred_final_answer[i])
        return final_answer