t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))
    tar = list(map(int, input().split()))

    present = {}
    absent = {}

    output = 0

    for i in range(len(tar)):
        if tar[i] in arr:
            present[arr.index(a)] = tar.index(a)
        # else:
        #     absent[arr.index(a)] = tar.index(a)

    for idx1, idx2 in present:
        output += abs(idx2 - idx1)

    for a in tar:
        if a not in arr:
            absent[arr.index(a)] = tar.index(a)



    for idx1, idx2 in absent:
        output += abs(idx2 - idx1)

    for


