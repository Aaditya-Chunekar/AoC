# brute(str) + prefix
ans=0
def pre(s1,s2):
    len=0
    while(s1[len]==s2[len]):
        len+=1
    return len
with open("day2.test","r") as f:
    # ranges=[]
    for line in f:
        ranges=(line.split(","))    
        for i in ranges:
            # s,e=[int(j) for j in i.split('-')]
            s,e=i.split('-')
            print(s,e)
            if(len(s)==len(e)):
                print(pre(s,e))
                # if both lengths are same 
                    # if both lengths are odd , skip it

                    #if both lengths are even
                        # if prefix size is >=half increment ans by 1
                    
                # if both lengths are diff.
                    # loop only for even lengths within the bounds
                    # example: smallest 4 digit number is 10 00
                    #          if upper bound is 1036 
                    #               ans+=1
                    #          but if upper bound is 1005 and lower 999, do nothing

    print(ranges)