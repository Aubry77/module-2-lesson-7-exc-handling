def f_to_c(f): return (f - 32) * 5/9

try:
    f = float(input("Temp in °F: "))
    print(f"{f}°F is {f_to_c(f):.2f}°C")
except ValueError:
    print("Oops! Numbers only, please.")
finally:
    print("Thanks for using our weather app!")
