import hashlib
ip="iwrupvqb"
start=10**len(ip)
ans=0
b=True
# text="abcdef609043"
# print(str(hashlib.md5(text.encode()).hexdigest())[:5].count('0')==5)
while(b):
    if(str(hashlib.md5((ip+str(start)).encode()).hexdigest())[:5].count('0')==5):
        ans=start
        b=False
    start+=1
print(start-1)
print(str(hashlib.md5("iwrupvqb101167331".encode()).hexdigest()))