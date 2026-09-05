ans=0
with open("day2.ip",'r') as f:
    for line in f:
        arr=list(map(int, line.split('x')))
        a1,a2,a3=arr[0]*arr[1],arr[1]*arr[2],arr[0]*arr[2]
        ans+=(2*(a1+a2+a3))+min(a1,a2,a3)
print(ans)
