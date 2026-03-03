##sal=int(input())
##exp=int(input())
##if(exp<2):
##     final=sal
##elif(exp>=2 and exp<=5):
##     final=sal+sal*0.1
##else:
##    final=sal+sal*0.2
##print(final)
###Digit pattern series
##print()
n=int(input())
series=[]
if n>=1:
     series.append(1)
for i in range(0,n-1):
     series.append((series[i]*10)+1)
print(*series)
     
