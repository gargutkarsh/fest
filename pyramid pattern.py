for i in range(1,6):
        for j in range(5-i,0,-1):
            print(" ",end=" ")
        for y in range(1,i+1):
            print(y,end=" ")
        for g in range(i-1,0,-1):
            print(g,end=" ")
        print("\n")
