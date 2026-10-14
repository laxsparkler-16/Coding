class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x==0:
            return 0

        a=x/2
        b=0
    
        while True:
            b=(a+x/a)/2
            if b==a:
                break
        
            a=b

        return int(b)
            