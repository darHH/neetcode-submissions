class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first find the row using top pointer and bottom pointer
        outer_len = len(matrix)
        inner_len = len(matrix[0])
        print(outer_len, inner_len)
        tp, bp = 0,  outer_len - 1
        outer_row_answer = 0
        while tp <= bp:
            outer_mp = (bp - tp) // 2 + tp
            # print("tp, bp, outer_mp", tp, bp, outer_mp)
            if matrix[outer_mp][0] == target or matrix[outer_mp][inner_len - 1] == target:
                return True
            elif matrix[outer_mp][0] < target and matrix[outer_mp][inner_len - 1] > target:
                outer_row_answer = outer_mp
                # print("1B")
                break
            elif matrix[outer_mp][0] > target:
                # print("1C")
                bp = outer_mp - 1
            else:
                # print("1D")
                tp = outer_mp + 1
        lp, rp = 0, inner_len - 1
        while lp <= rp:
            inner_mp = (rp - lp) // 2 + lp
            # print("lp, rp, inner_mp", tp, bp, inner_mp)
            if matrix[outer_row_answer][inner_mp] == target:
                return True
            elif matrix[outer_row_answer][inner_mp] < target:
                lp = inner_mp + 1
            else:
                rp = inner_mp - 1
        return False

