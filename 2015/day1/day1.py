ans=0
ansTwo=1
loc=0
with open("day1.ip",'r') as f:
    for line in f:
        ans+=line.count('(')-line.count(')')
        for c in line:
            if c=='(':
                loc+=1
            else:
                loc-=1
            if loc==-1:
                print("ansTwo",ansTwo)
                break
            ansTwo+=1

print(ans)
