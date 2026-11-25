class Solution:
    def checkIfPangram(self, sen: str) -> bool:
        return len(set(sen))==26
        