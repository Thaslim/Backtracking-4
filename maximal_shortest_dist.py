"""
Given a grid with w as width, h as height. Each cell of the grid represents a potential building lot and we will be adding "n" buildings inside this grid. The goal is for the furthest of all lots to be as near as possible to a building. Given an input n, which is the number of buildings to be placed in the lot, determine the building placement to minimize the distance the most distant empty lot is from the building. Movement is restricted to horizontal and vertical i.e. diagonal movement is not required.

For example, w=4, h=4 and n=3. An optimal grid placement sets any lot within two unit distance of the building. The answer for this case is 2.

"0" indicates optimal building placement and in this case the maximal value of all shortest distances to the closest building for each cell is "2".


TC: O(k^(N/k))
SP: O(H*W)
"""

def maximal_shortest_distance(width, height, num_buildings):
    grid = [[-1 for _ in range(width)] for _ in range(height) ]
    res = float('inf')
    def calc_dist(grid):
        q = deque()
        mat = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid)) ]
        rows, cols = len(mat), len(mat[0])
        directions = [(-1,0), (1,0), (0, -1), (0,1)]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i,j))
                # else:
                #     mat[i][j] = -1
        level = 0
        max_dist = -1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if 0<=nr<rows and 0<=nc<cols and mat[nr][nc]==-1:
                        mat[nr][nc]=level+1
                        max_dist = max(max_dist, level+1)
                        q.append((nr,nc))
            level+=1
        return max_dist
    
    def backtrack(i, j, count):

        nonlocal res
        if count >= num_buildings:
            res = min(res, calc_dist(grid))
            return 
        if j ==width:
            j = 0
            i+=1
        for l in range(i, height):
            for k in range(j, width):
                grid[l][k] = 0
                backtrack(l, k+1, count+1)
                grid[l][k] = -1
    backtrack(0, 0, 0)
    return res

print(maximal_shortest_distance(4, 4, 3))
                
    