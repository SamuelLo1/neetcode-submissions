class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        curr = []

        def backTrack(i,j): 
            
            boardVal = board[i][j]
            curr.append(board[i][j])
            currWord = ''.join(curr)

            print(i, j, currWord)

            if (currWord == word): 
                return True

            if (len(currWord) >= len(word)): 
                return False

            print(board[i][j], "word len",len(curr))

            board[i][j] = -1

            #loop through each direction, essentially create all the combinations with this
            for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]: 
                newRow = i + dx
                newCol = j + dy

                #check in bounds
                if (newRow < 0 or newRow >= len(board) or newCol < 0 or newCol >= len(board[0])): 
                    continue
                #check visited
                if (board[newRow][newCol] == -1 or board[newRow][newCol] != word[len(curr)]): 
                    continue
                #if in bounds: 
                if (backTrack(newRow, newCol)): 
                    return True
               

            curr.pop()
            board[i][j] = boardVal
            return False

        for i in range(len(board)): 
            for j in range(len(board[i])): 
                if (board[i][j] == word[0]): 
                    if(backTrack(i,j)): 
                        return True

        return False