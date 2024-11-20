#22.	Converte Fahrenheit para Celsius: Crie uma função 
# fahrenheit_para_celsius(fahrenheit) que converte uma temperatura em 
# Fahrenheit para Celsius.

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
temperatura_fahrenheit = 77
temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
print(temperatura_celsius)  # Saída: 25.0
