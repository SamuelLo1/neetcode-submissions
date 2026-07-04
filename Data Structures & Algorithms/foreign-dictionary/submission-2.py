class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        form directed edges where two pointers are not the same character

        when dealing with topological sorting: 
        always keep cycles in mind
        always keep visited nodes in mind

        things that can cause return of "" 
        - when the length of previous is greater than the one before but same prefix
        - logic does not make sense, there is a cycle within the array 
        """
        
        # form adj list for every character in all the words
        adj = {c: set() for w in words for c in w}
        # indegree list for each of the nodes
        indegree = {c: 0 for c in adj}

        left, right = 0, 1
        while (right != len(words)): 
            
            # get prefix of smaller word
            pref = min(len(words[left]), len(words[right]))
            if (words[left][:pref] == words[right][:pref] and len(words[left]) > len(words[right])): 
                return "" 
            # iterate through the characters whilst they are not equal
            # if we find something that is not the same then break 
            for j in range(pref): 
                if (words[left][j] != words[right][j]): 
                    if (words[right][j] not in adj[words[left][j]]):
                        adj[words[left][j]].add(words[right][j])
                        indegree[words[right][j]] += 1
                    break

            left += 1
            right += 1

        print(indegree)
        print(adj)
        # get all in degree with 0 if none then return ""
        # top sort
        # special: deque can popleft in O(1) time
        # typically parents and children 
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while q: 
            char = q.popleft()
            print("within q", char)
            res.append(char)
            # add to queue, and update 
            for neighbor in adj[char]: 
                indegree[neighbor] -= 1                
                if indegree[neighbor] == 0: 
                    q.append(neighbor)
        
        if len(res) != len(indegree): 
            return ""
        else: 
            return "".join(res)


