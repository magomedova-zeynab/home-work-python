def parse_number(value):
    return float(value)


if __name__ == "__main__":
    s = input("Введите число: ")
    try:
        n = parse_number(s)
    except ValueError:
        print("Некорректное значение: не удалось преобразовать в число")
    else:
        print(f"Получено число: {n}")