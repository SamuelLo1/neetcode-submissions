class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        given an integer array of nums: 
        return the sums of 3 elements where they all add up to 0

        sort the array
        this will allow traversal with two pointers easy. Check if the remaining element can be found in hashmap

        

        greatest in hashmap is 1 other than 2
        
        ensure the range from start to end includes at least 0 or a negative number
        get every possible pairing of sums, then loop through and check if 
        [-4,-1,-1,0,1,2]

            -1        2

        initial sort of array
        for each element in array can calculate 2-sum from that element
            - make sure to avoid repeated elements by continuing if traversed before
        """

        nums.sort()
        results = []



        def two_sum(i, target): 
            start = i + 1
            end = len(nums) - 1
            pairings = []
            while start < end:
                #skip dups
                if (start - 1 > i and nums[start - 1] == nums[start]):
                    print("skipping", start, nums[start]) 
                    start += 1
                    continue
                if (end + 1 <= len(nums) - 1 and nums[end + 1] == nums[end]): 
                    end -= 1
                    continue

                #equal, greater, less than cases
                curr_sum = nums[start] + nums[end]
                #print(curr_sum, nums[start], nums[end])
                if (curr_sum == target): 
                    pairings.append([-target, nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif (curr_sum < target): 
                    start += 1
                else: 
                    end -= 1
            return pairings


        for i, num in enumerate(nums):
            #skipping dups
            if (i - 1 >= 0 and nums[i-1] == nums[i]): 
                continue

            #run through two sum with the remaining partition of the array
            pairings = two_sum(i, -(num))
            #pair is found
            for pairing in pairings: 
                results.append(pairing)
            
            
        return results
