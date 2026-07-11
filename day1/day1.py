b,l,r=50,0,99
ans=0
ansb=0
with open("day1.ip","r") as f:
    for line in f:
        # print('-'*10)
        v=int(line[1:])
        # print(line, v)
        if(line[0]=="R"):
            total = b + v
            # MAKING A SEPARATE total VARIABLE was necessary
            ansb += total // 100
            b = total % 100
        else: 
            # "this is a very important block"
            first = b if b != 0 else 100
            if v >= first:
                ansb += (v - first) // 100 + 1
            b = (b - v) % 100
        if(b==0):
           ans+=1
        # print("b",b)
        #    ansb+=1
print(ans,ansb)

'''
 after the granting of star, 
 git add .; git commit -m "dayOne"; git push
'''