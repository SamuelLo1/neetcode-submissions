class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        return all substrings where each character is a palindrome
        essentially brute force partitions

        want to continue to form check substrings while palindrome 
                    []
                   a  []
        
        how is substring formed? 
        j, i is the partition of the substring? 
        
        we increase the window by 1 at the end of palindrome searching 
        from the current path

        """
        res = []
        part = []

        # since every part of the string needs to exist, start from begginning
        # and recursively build substring by adding one character and trying all additional characters 
        # backtracking all substring combinations
        def dfs(i): 
            # if the i is past end, this means that is was palindrome till then and can be added
            # in backtracking can be sure that there are no duplicates, because each decision tree is
            # different path and needs to continue 
            if i >= len(s): 
                res.append(part.copy())
                return
            
            # loop through all possible substring that can form valid palindromes
            for j in range(i, len(s)): 
                if self.isPali(s, i, j): 
                    part.append(s[i:j + 1])
                    print(part)
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res

    def isPali(self, s, l, r): 
        while l < r: 
            if (s[l] != s[r]): 
                return False
            else: 
                l += 1
                r -= 1
        return True

            
