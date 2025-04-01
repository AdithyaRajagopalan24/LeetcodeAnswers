class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowsCount = len(board)
        columnsCount = len(board[0])
        if len(word) > rowsCount*columnsCount:
            return False
        
        count = Counter(sum(board, []))
        
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
            
        if count[word[0]] > count[word[-1]]:
             word = word[::-1]
                        
        checked = set()
        
        def searching(rows, columns, i):
            if i == len(word):
                return True
            if rows < 0 or columns < 0 or rows >= rowsCount or columns >= columnsCount or word[i] != board[rows][columns] or (rows,columns) in checked:
                return False
            
            checked.add((rows,columns))
            res = (searching(rows+1,columns,i+1) or searching(rows-1,columns,i+1) or searching(rows,columns+1,i+1) or searching(rows,columns-1,i+1))
            checked.remove((rows,columns))  #backtracking

            return res
        
        for i in range(rowsCount):
            for j in range(columnsCount):
                if searching(i,j,0):
                    return True
        return False