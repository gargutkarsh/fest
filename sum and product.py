val=str(input())
sum=0
pro=1
while(val!='Q'):
    if val.isdigit():
        N = int(val)
        if(N%2==0):
            sum=sum+N
            print("sum is",sum)
            val=str(input())
        elif(N%2!=0):
            pro=pro*N
            print("product is",pro)
            val = str(input())


    
