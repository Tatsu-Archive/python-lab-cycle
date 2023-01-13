def check_happy(n):
  i=0#Used to check how many times the loop works
  while(n!=1):
    a,s=n,0
    while(a>0):
      r=a%10
      s=s+r*r#To add up the sum of squares of the digits
      a=a//10
    n=s#To change the value of n to the sum of squares of the digits
    i=i+1
    if(i>100):
      break
  if((n==1)and(n<100)):
    return True #Return true if it is a happy number
  else:
    return False #Return false if the number is a sad number

n=int(input("Enter a number:"))
bo=check_happy(n)
if(bo==True):
  print("The number is a happy number")
else:
  print("The number is a sad number")