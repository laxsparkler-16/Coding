class Solution:
    def reverse(self, x: int) -> int:

        aa=-1 if x<0 else 1
        a=abs(x)
        b=0
        while(a>0):
            b=b*10+a%10
            a//=10

        print(aa*b,"zx")
        if aa*b<-2**31 or aa*b>2**31-1:
            return 0
        
        return aa*b