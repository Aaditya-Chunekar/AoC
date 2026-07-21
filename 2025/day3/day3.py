ans=0
with open("day3.test","r") as f:
    for line in f:
        s=sorted(line)
        print(s)
        print((s[-2]))
        ans+=int(s[-2])*10+int(s[-1])
print(ans)


    