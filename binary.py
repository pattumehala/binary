a=raw_input()
n=len(a)
p=0
for i in range(0,n):
  if(a[i]=='0' or a[i]=='1'):
    p+=1
if(n==p):
  print("yes")
else:
  print("no")
