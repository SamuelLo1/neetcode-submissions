class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        return length of longest common subsequence

        subsequence: still in order but not necessarily consecutive 
        
        find subsequence that exists in both strings

        if equal then, make the length same 

        put each word of subsequence up agains the next and think in partitions. 
        if the previous partition not including the current character can have longest subsequence
        of certain characters, then what would it be with the current character. 

        form a 2d dp array: 
        we will take partitions of each string and check the max possible 
        common subsequence from the previous partition 
            cat 
        c   
        r
        a
        b      
        t.  111
        """

        m = len(text1) + 1
        n = len(text2) + 1

        dp = [[0] * (n) for i in range(m)]
        
        for i in range(m - 1, -1, -1): 
            for j in range(n - 1, -1, -1):
                if (i == m - 1): 
                    dp[i][j] = 0
                    continue
                if (j == n - 1): 
                    dp[i][j] = 0
                    continue

                # character is equal 
                if (text1[i] == text2[j]): 
                    dp[i][j] = 1 + dp[i + 1][j + 1] 
                    continue
                
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1]) 
                
        return dp[0][0]

        