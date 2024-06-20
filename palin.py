def check(n):
    
    val=True
    while(val):
        if(n==n[::-1]):
            print(len(n))
            val=False
        else:
            h=int(n)+int(n[::-1])
            print(h)
            n=str(h)
            
    
n=input("enter a number")
check(n)
