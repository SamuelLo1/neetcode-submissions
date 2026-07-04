class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        return true if word present 
        same cell not used more than once

        need to go in a direction and backtrack if not found
        use dfs

        terminate if next letter in word not found
        start dfs when first letter of character found
        """

        n = len(board)
        m = len(board[0])

        visited = set()
        def backtrack(i, j, k): 
            """
            dfs all the directions make sure to subtract from current index of char looking for

            """
            directions = [(0,1) , (1,0) , (-1,0), (0,-1)]
            print("inside backtrack")
            # have matched all characters
            if (k == len(word)): 
                return True
            visited.add((i,j))
            for dx, dy in directions: 
                new_x = i + dx 
                new_y = j + dy 

                print()
                # within bounds
                if (new_x >= 0 and new_x < n and new_y >= 0 and new_y < m): 
                    if (board[new_x][new_y] == word[k] and (new_x, new_y) not in visited): 
                        if (backtrack(new_x, new_y, k + 1)):
                            print("exploring", new_x, new_y)
                            return True

            visited.remove((i,j))
            return False

        for i in range(n): 
            for j in range(m): 
                # check if word can be formed here
                if (board[i][j] == word[0]):
                    if (backtrack(i, j, 1)): 
                        return True
        
        return False
        
