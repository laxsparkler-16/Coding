class Solution:
    def isPalindrome(self, s: str) -> bool:
        a="".join(i.lower() for i in s if i.isalnum())
        

        # print(f"{a}\n{a[::-1]}")

        if a==a[::-1]:
            return True
        else:
            return False