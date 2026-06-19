# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

heights = [2,1,5,6,2,3]
areas = []


# This is the brute force approach that I came up with on my own
for i in range(len(heights)):
    width_r = 0
    width_l = 0
    for j in range(len(heights)-i-1):
        if heights[i+j+1] >= heights[i]:
            width_r += 1
        else:
            break
    for k in range(i):
        if heights[i-k-1] >= heights[i]:
            width_l += 1
        else:
            break
    areas.append((width_r + width_l + 1)*heights[i])
print(max(areas))

"""
But this was showing TLE for large array lengths. Time complexity of this is O(n^2),
and this is bad, since n is given to be at most 10^5.



"""

for i in range(len(heights)):
    prevSmallestVal = -1
    prevSmallestIdx = 0
