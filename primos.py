def prime_check(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, num):
        if (num % i) == 0:
            return False
    else:
        return True
def highest_prime(num):
    if num < 2:
        print("Digite um número maior ou igual a 2.")
    prime = -1
    for i in reversed(range(num)):
        if prime_check(i) is True:
            prime = i
            break
    if prime == num:
        print(f"Não tem número primo menor que {num}.")
    else:
        print(f"O menor número primo é {prime}.")
        
