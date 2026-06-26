# https://leetcode.com/problems/product-of-array-except-self/description/

'''
They said 'without using division operation' and in O(n) time

If we could use division, then the problem would be trivial, with each element being prod/arr[i]

But, think how to do without division...

Hint: try and reduce 'double counting' (ie, try not to recompute what has already been computed)

'''


nums = [-1,1,0,-3,3]

l_prod = []
r_prod = []

prod = 1
for num in nums:
    prod *= num
    l_prod.append(prod)
print(l_prod)

prod = 1
for num in reversed(nums):
    prod *= num
    r_prod.append(prod)
print(r_prod)
l_prod.insert(0, 1)
r_prod.reverse()
r_prod.pop(0)
r_prod.append(1)

out = [0] * len(r_prod)
for i in range(len(r_prod)):
    out[i] = l_prod[i]*r_prod[i]

print(out)
