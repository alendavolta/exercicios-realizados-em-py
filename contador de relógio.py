
x = int(input("Por favor, entre com o número de segundos que deseja converter:"))
a = x//86400
b = x%86400//3600
c = x%86400%3600//60
d = x%86400%3600%60

print (a, "dias,", b, "horas,", c,"minutos,", d,"segundos,")

