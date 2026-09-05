ans=0
with open("day1.ip",'r') as f:
    for line in f:
        ans+=line.count('(')-line.count(')')
print(ans)
