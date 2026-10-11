class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet="abcdefghijklmnopqrstuvwxyz0123456789"
        clean_s=s.lower()
        string=''
        for i in clean_s:
            if i in alphabet:
                string=string+i
            else: 
                continue
        tuple_string=tuple(string)
        for i in range(len(tuple_string)//2):
            if tuple_string[i]!=tuple_string[-(i+1)]:
                return False
        return True
