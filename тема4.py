from add import calculate_area

def main():
    try:
        a = float(input("Введите первую длину: "))
        b = float(input("Введите вторую длину: "))
        c = float(input("Введите третью длину: "))

        area = calculate_area(a, b, c)
        print("Площадь треугольника:", area)

    except ValueError as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()
