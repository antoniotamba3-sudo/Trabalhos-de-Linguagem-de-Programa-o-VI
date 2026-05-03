
def is_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def gerador_primos(limite):
    num = 2
    while num <= limite:
        if is_primo(num):
            yield num
        num += 1
print("\n--- Gerador de Primos ---")
print("Primos até 1000:")
for primo in gerador_primos(1000):
    print(primo, end=" ")
print()
print("Primos até 200:")
primos = list(gerador_primos(200))
print(primos)