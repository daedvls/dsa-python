'''
https://leetcode.com/problems/pascals-triangle/
'''

numRows = int(input())

output = []
for row in range(numRows):
    if row==0:
        output.append([1])
    elif row==1:
        output.append([1, 1])
    else:
        out = [1]
        for i in range(row-1):
            out.append(output[row-1][i] + output[row-1][i+1])
        out.append(1)
        output.append(out)


for ele in output:
    for element in ele:
        print(element, end=" ")
    print()
