class Solution:

    #encoding the strings would just be adding them together
    """
    method 1:
    "keep track of sizes of each string and keep it before the rest of the appended strings"
    "this will allow to know how much to increment i each time" 

    method 2: 
    "turn all strings into digits and seperte each character" : O(m * n)
    """
    def encode(self, strs: List[str]) -> str:
        if not strs: 
            return ""

        #get the sizes of each string
        seperator = ","
        encoded_str, sizes = "", []

        for i in range(len(strs)):
            sizes.append(len(strs[i]))

        for i in range(len(sizes)): 
            encoded_str += str(sizes[i])
            encoded_str += ","
        
        #sperate sizes and characters
        encoded_str += "#"
        for s in strs: 
            encoded_str += s
        
        return encoded_str



    #reconstruct the sizes array and add each string to results
    def decode(self, s: str) -> List[str]:
        if not s: 
            return []

        res, sizes = [], []

        #reconstruct the sizes array
        i = s.find("#")
        sizes = s[0: i].split(",")
        sizes.pop()
        print(sizes)
        for sz in sizes: 
            res.append(s[(i + 1): (i + int(sz) + 1)])
            i += int(sz)
        return res


        
        
        