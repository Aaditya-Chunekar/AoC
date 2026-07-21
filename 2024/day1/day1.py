lt=[]
rt=[]
with open("day1.ip",'r') as f:
    for line in f:
        nums=line.split()
        rt.append(int(nums[1]))
        lt.append(int(nums[0]))
lt=sorted(lt)
rt=sorted(rt)
ans=0
for i in range(len(lt)):
    ans+=abs(lt[i]-rt[i])
print(ans)
