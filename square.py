n=input("enter a number")
s=''
for i in range(len(n)):
    if i%2==1:
        s=s+str(int(n[i])**2)
        print(s[:4])
