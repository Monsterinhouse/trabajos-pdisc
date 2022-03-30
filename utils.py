def suma(numeros) : 
    sum = 0

    for num in numeros:
        sum += num

    return sum


def prom(numeros):

    promedio = suma(numeros) / len(numeros)

    return promedio


