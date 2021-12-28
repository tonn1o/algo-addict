class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        degDict = dict()
        maxDeg = 0
        res = math.inf
        
        for i, num in enumerate(nums):
            if num in degDict:
                degDict[num]["deg"] += 1
                degDict[num]["end"] = i
            else: 
                degDict[num] = {"start": i, "end": i, "deg": 1}
            
            if degDict[num]["deg"] > maxDeg: 
                maxDeg = degDict[num]["deg"]
                res = math.inf
            
            if degDict[num]["deg"] == maxDeg:
                res = min(res, degDict[num]["end"] - degDict[num]["start"] + 1)
            

        return res
     
# Alternative implementation   
class Solution(object):
    def findShortestSubArray(self, nums):
        degree = 0
        
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
            degree = max(degree, count[x])

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
