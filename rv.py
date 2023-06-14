n =int(input('Enter\n'))
rev=0
sum =0
while(n>0):
    digit = n % 10
    rev = rev * 10 + digit
    sum = sum + digit
    n = n // 10
print(rev)
print(sum)