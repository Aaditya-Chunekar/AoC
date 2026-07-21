# binary search might be a better way to do this
ranges=[]
nums=[]
with open("day5.test","r") as f:
    for line in f:
        if '-' in line:
            numStr=line.split('-')
            ranges.append((int(numStr[0]),int(numStr[1])))
        elif line[:-1]!='':
            nums.append(int(line[:-1]))
# print(ranges)
# print(nums)


