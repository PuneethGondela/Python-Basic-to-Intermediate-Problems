print("Even Sum of Numbers\nEnter the Number:")
num=int(input())
s=0
for i in range(1,num+1):
  if i%2==0:
      s+=i
print("Sum of Even Numbers",s)