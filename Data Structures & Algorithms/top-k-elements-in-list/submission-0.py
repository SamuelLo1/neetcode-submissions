class Solution:


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        can store a hashmap, then sort by values and return the keys

        is nums always sorted or not 
        
        say we have a list of tuples of an value and its freq
        we can loop through the tuple and append values. 
        keeping an array of size k. Where the smallest element is kept track of and popped when a bigger element is found. can use a minheap? 

        can store each value and the bucket count of that value
        use a 2d array
        """
        #for each value store inside a bucket based on frequency
        freq_list = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        
        #get frequencies and store into buckets
        for num in nums: 
            if num not in freq_list: 
                freq_list[num] = 1
            else: 
                freq_list[num] += 1

        #populate buckets 
        for key, value in freq_list.items():
            buckets[value].append(key)
        
        print(buckets)
        results = []
        i = len(nums)

        #reverse traversal through buckets
        while i > 0: 
            if (len(buckets[i]) != 0): 
                #pop through elements in a bucket
                while (len(buckets[i]) > 0): 
                    results.append(buckets[i].pop())
                    k -= 1
                    if (k == 0):
                        return results
            i -= 1
        return results