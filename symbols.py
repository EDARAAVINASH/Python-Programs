s=input()
d=dict()
res=''
for i in range(len(s)):
    if s[i].isalnum()==False:
        d.update({i:s[i]})
    else:
        res+=s[i]
res=list(res[::-1])
for i,j in d.items():
    res.insert(i,j)
print(“”.join(res))


