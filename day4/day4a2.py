t,ip=10,137
def partOne(fileName, h):
    tt=[]
    for i in range(h):
        tt.append([0]*h)
    # print(tt)
    dept=[]
    # perRow=[5,1,1,0,2,0,0,1,0,3]
    ans=0
    with open(fileName,"r") as f:
        for line in f:
            dept.append(line[:-1])
    # print(dept)
    for i in range(0,h):
        for j in range(0,h):
            if dept[i][j]=='@':
                # print("-"*10)
                # print(i,j,"\n---\n")
                dr=[1,0,1, 1]
                dc=[0,1,1,-1]
                for k in range(len(dc)):
                    nr=i+dr[k]
                    nc=j+dc[k]
                    if(0<=nr<h and 0<=nc<h):
                        if(dept[nr][nc]=='@'):
                            tt[i][j]+=1
                            # print(nr,nc)
                            tt[nr][nc]+=1
            else:
                tt[i][j]=4
    for i in tt:
        ans+=sum(1 for x in i if x<4)
    return ans
print(partOne("day4.ip",ip))




