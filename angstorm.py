n=input()
sum=0
if (len(n)==3):
    for i in str(n):
        if i.isdigit():
            c=int(i)*int(i)*int(i)
            sum=sum+c
    if (int(n)==sum):
         print("number is angstorm")
    else:
         print("number s not angstorm")
else:
    print("not a 3 digit number")



