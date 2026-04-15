#Write a program using function to convert Celsius to Fahrenheit.

def temp_conv(n):
    return (9/5) * n + 32
n = int(input("Enter temperature in Celsius: "))
print(f"Celsius to Fahrenheit = {round(temp_conv(n),2)} °C")

