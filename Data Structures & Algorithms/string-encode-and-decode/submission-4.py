class Solution:

    def encode(self, strs: list[str]) -> str:
        answer=''
        for i in range(len(strs)):
            answer=answer+str(len(strs[i]))+" "+strs[i]
        return answer
    
    def decode(self, s: str) -> list[str]:
        answer=[]
        i=0
        num=''
        while i<len(s):
            if s[i]!=' ':
                num=num+s[i]
                i+=1
            else:
                answer.append(s[i+1:i+1+int(num)])
                i=i+1+int(num)
                num=''
        return answer 
