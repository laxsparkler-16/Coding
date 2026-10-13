class Solution:
    def reverseWords(self, s: str) -> str:
        
        str=s.split()
        str.reverse()
        # for i in reversed(str):
        #     print(i,end=" ")

        return " ".join(str)