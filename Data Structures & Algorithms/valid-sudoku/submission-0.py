class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for i in range(9)]
        col=[set() for i in range(9)]
        box=[set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                k=(i//3)*3 + (j//3)
                num=board[i][j]
                if num ==".":
                    continue
                if num in row[i] or num in col[j] or num in box [k]:
                    return False
                else:
                    row[i].add(num)
                    col[j].add(num)
                    box[k].add(num)

        return True

        