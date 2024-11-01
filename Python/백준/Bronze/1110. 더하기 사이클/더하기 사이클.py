n1 = int(input())
n2 = n1

sum = 0
count = 0

while 1:
   sum = n2 // 10 + n2 % 10
   n2 = (n2 % 10) * 10 + sum % 10
   count += 1
   if n2 == n1:
       break

print(count)




