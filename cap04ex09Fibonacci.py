'''def fibonacci_ate(n):
    lista = [0, 1]
    for i in range(2, n):
        prox = lista[i-1] + lista[i-2]
        lista.append(prox)
    return lista[:n]

print(fibonacci_ate(20))'''

def fibonacci_ate(n):
    lista = [0, 1]
    
    while True:
        prox = lista[-1] + lista[-2]
        if prox <= n:
            lista.append(prox)
        else:
            break
    return lista

print(fibonacci_ate(1000))