def suma (a,b):
    return a + b

print(suma(5,7))

def resta (a,b):
    return a - b

print(resta(10,4))

def multiplicacion (a,b):
    return a * b    

print(multiplicacion(3,5))

def division (a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print(division(10,2))

def potencia (a,b):
    return a ** b

print(potencia(2,3))

def modulo (a,b):
    if b == 0:
        return "Error: Division by zero"
    return a % b

print(modulo(10,3))
