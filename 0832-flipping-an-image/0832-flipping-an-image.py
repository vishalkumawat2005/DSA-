class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                if row[i]==0:
                    row[i]=1
                else:
                    row[i]=0
        return image