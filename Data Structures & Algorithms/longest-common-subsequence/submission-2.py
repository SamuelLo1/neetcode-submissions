class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        
        return longest common subsequence etween two strings

        - since t may be found before 'a' 
        - would need to consider using diff combos of letters 
        - brute force: could backtrack all combos and check all combos to see which works and has least 

        - dynamic programming? 
            with string probs pointers is best

            cat 
              i    
            crabt
                j

            can either consider a char or not 

            if either i or j increment past then return 
             ( try next if there is a next character to try)

            accumulate as I go 

            ""
            asdfsaf


            abcd
               i
            efgh
               j

            the dfs is keeping track of how j changes with i
            we want to make sure to return the max of (i, j) the maximum possible subarray from i, j
            can memoize i and j 

        """
        n, m = len(text1), len(text2)
        memo = {}


        def dfs(i, j): 
            if i == n or j == m: 
                return 0 
            
            if (i, j) in memo: 
                return memo[(i,j)]
            
            if (text1[i] == text2[j]): 
                memo[(i,j)] = 1 + dfs(i+1, j+1)

            else: 
                # consider don't use current i from text1
                # consider use current i from text1 but not compare with current j
                # don't need for loop to check every j, for each character, think of the problem as a 
                # substring problem where I am trying to match a character inside substring
                # 
                memo[(i,j)] = max(dfs(i + 1,j), dfs(i, j+1))
            return memo[(i,j)]
            
        return dfs(0,0)
        

        