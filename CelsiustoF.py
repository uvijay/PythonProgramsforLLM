def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return "That temperature doesn't make sense!"
    else:
        return (celsius * (9/5)) + 32
print(celsius_to_fahrenheit(56))
