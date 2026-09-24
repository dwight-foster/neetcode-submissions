class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c = 0
        while c < len(matrix[0]):
            l, r = 0, len(matrix)- 1
            while l < r:
                mid = (l + r)//2
                if matrix[mid][c] == target:
                    return True
                elif matrix[mid][c] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            if matrix[l][c] == target:
                return True
            c += 1
        
        return False