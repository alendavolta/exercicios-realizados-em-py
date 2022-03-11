x = int(input("Digite um número inteiro:"))

a = 0

while x>0:
    r =x%10
    x=(x-r)/10
    a=a+r

print (a)
