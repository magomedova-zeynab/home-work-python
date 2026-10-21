def process_large_file(path):
    count = 0
    total = 0
    min_val = None
    max_val = None

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                num = int(line)
            except ValueError:
                continue
            count += 1
            total += num
            if min_val is None or num < min_val:
                min_val = num
            if max_val is None or num > max_val:
                max_val = num

    if count == 0:
        print("Файл пуст или не содержит чисел")
        return

    print(f"Сумма: {total}")
    print(f"Минимум: {min_val}")
    print(f"Максимум: {max_val}")
    print(f"Количество: {count}")
    print(f"Среднее: {total / count}")


process_large_file("big_numbers.txt")