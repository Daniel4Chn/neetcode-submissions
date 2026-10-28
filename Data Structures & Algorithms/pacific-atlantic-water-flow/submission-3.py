class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pac = set()
        atl = set()
        res = []

        def dfs(i, j, prev, setOfOcean):
            if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0]) or (i, j) in setOfOcean or heights[i][j] < prev:
                return
            setOfOcean.add((i,j))
            dfs(i+1, j, heights[i][j], setOfOcean)
            dfs(i-1, j, heights[i][j], setOfOcean)
            dfs(i, j-1, heights[i][j], setOfOcean)
            dfs(i, j+1, heights[i][j], setOfOcean)
        
        for c in range(len(heights[0])):
            dfs(0, c, heights[0][c], pac)
            dfs(len(heights)-1, c, heights[len(heights)-1][c], atl)
        
        for r in range(len(heights)):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, len(heights[0])-1, heights[r][len(heights[0])-1], atl)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in atl and (i, j) in pac:
                    res.append([i,j])
        
        return res
