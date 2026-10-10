class Solution:
    def reverseVowels(self, s: str) -> str:
        
        ss=list(s)

        a=0
        b=len(s)-1
        vow=set("aeiouAEIOU")
        while a<b:
            if ss[a] in vow and ss[b] in vow:
                # print(f"{ss[a]} {ss[b]}")
                c=ss[a]
                ss[a]=ss[b]
                ss[b]=c
                a+=1
                b-=1
            elif ss[a] in vow and ss[b] not in vow:
                b-=1
            else:
                a+=1

        
        return "".join(ss)