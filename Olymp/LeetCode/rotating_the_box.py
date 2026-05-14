class Solution:
    def rotateTheBox(self, boxGrid):
        n, m = len(boxGrid), len(boxGrid[0])
        for i in range(n):
            l = 0
            r = 0
            while r != m:
                if boxGrid[i][r] != '*':
                    boxGrid[i][l], boxGrid[i][r] = boxGrid[i][r], boxGrid[i][l]
                    if boxGrid[i][l] != '#':
                        l += 1 
                    r += 1
                else:
                    r += 1
                    l = r
        boxGrid = [list(reversed(line)) for line in zip(*boxGrid)]
        return boxGrid