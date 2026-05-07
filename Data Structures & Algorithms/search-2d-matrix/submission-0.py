class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get the row index first using binary search...
        startrowidx = 0
        endrowidx = len(matrix) - 1
        searchinthiscol = False
        while startrowidx <= endrowidx:
            midrowidx = (startrowidx + endrowidx) // 2
            if matrix[midrowidx][0] == target:
                return True 
            elif target < matrix[midrowidx][0]:
                endrowidx = midrowidx - 1
            elif target > matrix[midrowidx][0]:
                if target > matrix[midrowidx][len(matrix[midrowidx]) - 1]:
                    startrowidx = midrowidx + 1
                elif target == matrix[midrowidx][len(matrix[midrowidx]) - 1]:
                    return True 
                elif target < matrix[midrowidx][len(matrix[midrowidx]) - 1]:
                    searchinthiscol = True
                    break 
        
        # search in (rowidx = midrowidx)
        if searchinthiscol == True:
            startcolidx, endcolidx = 0, len(matrix[midrowidx]) - 1
            while startcolidx <= endcolidx:
                midcolidx = (startcolidx + endcolidx) // 2
                if target == matrix[midrowidx][midcolidx]:
                    return True 
                elif target < matrix[midrowidx][midcolidx]:
                    endcolidx = midcolidx - 1
                elif target > matrix[midrowidx][midcolidx]:
                    startcolidx = midcolidx + 1
        else:
            return False 
        
        return False 


        