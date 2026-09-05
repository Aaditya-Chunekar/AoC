ans=0
ansTwo=0
with open("day2.ip",'r') as f:
    for line in f:
        arr=list(map(int, line.split('x')))
        a1,a2,a3=arr[0]*arr[1],arr[1]*arr[2],arr[0]*arr[2]
        p1,p2,p3=arr[0]+arr[1],arr[1]+arr[2],arr[0]+arr[2]
        ans+=(2*(a1+a2+a3))+min(a1,a2,a3)
        ansTwo+=(arr[1]*arr[0]*arr[2])+2*min(p1,p2,p3)
print(ans,ansTwo)
