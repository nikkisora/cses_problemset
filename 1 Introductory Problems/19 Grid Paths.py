'''

CSES - Grid Paths



Time limit: 1.00 s
Memory limit: 512 MB

There are 88418 paths in a 7 \times 7 grid from the upper-left square to the lower-left square. Each path corresponds to a 48-character description consisting of characters D (down), U (up), L (left) and R (right).


For example, the path


corresponds to the description DRURRRRRDDDLUULDDDLDRRURDDLLLLLURULURRUULDLLDDDD.


You are given a description of a path which may also contain characters ? (any direction). Your task is to calculate the number of paths that match the description.

Input


The only input line has a 48-character string of characters ?, D, U, L and R.

Output


Print one integer: the total number of paths.

Example


Input:
??????R??????U??????????????????????????LD????D?


Output:
201 
'''

#every optimisation is implemented, runtime error due to limitations of a language

ans = 0

def path(step, mask, x, y, grid):
    ans = 0
    
    def isOk(x, y, grid):
        return x >= 1 and y >= 1 and x <= 7 and y <= 7 and not (grid & (1 << ((y-1)*7+x-1)))
    
    grid |= 1 << ((y-1)*7+x-1)
    
    if step == len(mask):
        if x == 7 and y == 1:
            return 1
        else:
            return 0
    elif x == 7 and y == 1:
        return 0
    
    c = mask[step]
    if c == '?' or c == 'L':
        if(isOk(x+1, y, grid) and not(not isOk(x+2, y, grid) and isOk(x+1, y+1, grid) and isOk(x+1, y-1, grid))):
            ans += path(step + 1, mask, x+1, y, grid)
    if c == '?' or c == 'R':
        if(isOk(x-1, y, grid) and not(not isOk(x-2, y, grid) and isOk(x-1, y+1, grid) and isOk(x-1, y-1, grid))):
            ans += path(step + 1, mask, x-1, y, grid)
    if c == '?' or c == 'U':
        if(isOk(x, y+1, grid) and not(not isOk(x, y+2, grid) and isOk(x+1, y+1, grid) and isOk(x-1, y+1, grid))):
            ans += path(step + 1, mask, x, y+1, grid)
    if c == '?' or c == 'D':
        if(isOk(x, y-1, grid) and not(not isOk(x, y-2, grid) and isOk(x+1, y-1, grid) and isOk(x-1, y-1, grid))):
            ans += path(step + 1, mask, x, y-1, grid)
    
    return ans

mask = input()
ans = path(0, mask[:], 7, 7, 0)
print(ans)