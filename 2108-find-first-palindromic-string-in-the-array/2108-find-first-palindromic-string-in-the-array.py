class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for i in words:
            rev=i[::-1] 
            if rev==i:
                return i
           
        return ""