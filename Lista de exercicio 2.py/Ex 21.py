#21.	Converte Celsius para Fahrenheit: Escreva uma função 
# celsius_para_fahrenheit(celsius) que converte uma temperatura em Celsius 
# para Fahrenheit.

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32
temperatura_celsius = 25
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(temperatura_fahrenheit)  # Saída: 77.0
