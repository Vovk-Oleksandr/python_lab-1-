a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

results = []
results.append(a + b)       # Додавання
results.append(a - b)       # Віднімання
results.append(a * b)       # Множення
results.append(a / b)       # Ділення
results.append(a ** b)      # Піднесення до ступеня
results.append(a // b)      # Цілочисельне ділення
results.append(a % b)       # Остача від ділення

print("Результати обчислень:")
print(results)
