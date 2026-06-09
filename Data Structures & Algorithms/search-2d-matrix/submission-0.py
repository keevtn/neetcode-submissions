class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        ro = len(matrix) - 1
        # outer ("check per row"), we binary search until we find a row whose bounds holds our target.
        while (lo <= ro):
            mo = lo + (ro - lo) // 2
            # if target in bounds, we do binary search on the row, until either target is found or not found.
            if matrix[mo][0] <= target <= matrix[mo][-1]:
                li = 0
                ri = len(matrix[mo]) - 1
                while (li <= ri):
                    mi = li + (ri - li) // 2
                    if matrix[mo][mi] == target:
                        return True
                    elif matrix[mo][mi] < target:
                        li = mi + 1
                    else:
                        ri = mi - 1
                return False
            elif matrix[mo][0] < target:
                lo = mo + 1
            else:
                ro = mo - 1
        return False