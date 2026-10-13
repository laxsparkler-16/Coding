class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        a=0
        b=len(s)-1

        while(a<b):
            c=s[a]
            s[a]=s[b]
            s[b]=c
            a+=1
            b-=1

        return s