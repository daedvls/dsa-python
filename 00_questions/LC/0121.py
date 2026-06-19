# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


# most optimal solution by me


prices = [7, 1, 5, 3, 6, 4]

s = 0
b = 0
profit = 0
for i in range(len(prices)):
    if prices[i] <= prices[b]:
        b = i
        s = i
        continue
    s = i
    profit = max(profit, (prices[s]-prices[b]))

print(profit)


'''
Notice that we don't actually even need s. Since s = i is being written in code in both cases
Note that s is a pointer representing sell and b is representing buy

Better code: (Same as Kadane's Algo)


b = 0
profit = 0
for i in range(len(prices)):
    if prices[i] <= prices[b]:
        b = i
        continue
    profit = max(profit, (prices[i]-prices[b]))

print(profit)
'''