n=int(input("Digite um número:"))
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(f"Fibonacci de {(n)} é :{fibonacci(n)}")

