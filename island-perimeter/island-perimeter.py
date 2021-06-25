class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for row_idx, row in enumerate(grid):
            for col_idx, land in enumerate(row):
                if not land:
                    continue
                perimeter += 4
				# If previous cell in the current row is land, reduce the perimeter by 2
                if col_idx and row[col_idx - 1]:
                    perimeter -= 2
				# If current column index of the previous/above row is land, reduce the perimeter by 2
                if row_idx and grid[row_idx - 1][col_idx]:
                    perimeter -= 2
        return perimeter