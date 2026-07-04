class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """

        - two strings 
        - lowercase eng letters

        - insert, delete, replace chars 
            - replace is a combo of insert + delete at same position
        

        Thinking: 
            - alwayas possible for word1 to reach word2
            - bounded by max, word2 or word1
            - characters shouldn't be removed naively some mgiht be needed to form minimum decisions

            - how to get the minimum number of decisions to reach word2? 
            

            memo = {from an index, how many changes it takes to get to the substring word}


            Brute force: 
                - for any character, can either insert, delete, or replace
                - as long as it matches, can move onto next 
                
                mmmmonkey money

                m matches m -- match means I don't need to use a decision
                continue 
                mm -- mo 

                mm matches
                mo mo matches
                mon mon matches
                monk mone does not match
                    perform decision tree (don't go down bad decisions)
                        mone --> mone --> monek

                continue exploring on paths that don't work
        """
        
        # can memoize curr_str : min decisions to reach word2
        # can use linked list for o(1) insert/ deletes 

        memo = {} # (i,j) : decisiosn to complete

        def dfs(i, j): 
            # word 1 is complete word 2 is not
            if (i == len(word1) and j != len(word2)): 
                return (len(word2) - j)

            # word 2 is complete word 1 is not 
            if (i != len(word1) and j == len(word2)): 
                return (len(word1) - i)

            # word 1 and word 2 are complete and equal 
            if (i == len(word1) and j == len(word2)): 
                print("finished")
                return 0 

            if (i,j) in memo: 
                return memo[(i,j)]

            # best possible scenario
            if (word1[i] == word2[j]): 
                memo[(i,j)] = dfs(i + 1, j + 1) + 0
                return memo[(i,j)]

            # remove currecnt char
            min_cost = min(dfs(i + 1, j), dfs(i, j + 1)) + 1
            min_cost = min(min_cost, dfs(i + 1, j + 1) + 1)
            memo[(i,j)] = min_cost
            return memo[(i,j)]

        return dfs(0,0)

        
            


