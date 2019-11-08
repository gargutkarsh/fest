string=input()
s=string[len(string)-1]
i=len(string)-2
while i>=0:
    s=s+string[i]
    i=i-1
print(s)
if s==string:
    print("string is palindrome")
else:
    print("string is not palindrome")

