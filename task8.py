def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Ошибка: файл не найден")
    except PermissionError:
        print("Ошибка: нет прав доступа к файлу")
    except IsADirectoryError:
        print("Ошибка: указанный путь является каталогом")
    except UnicodeDecodeError:
        print("Ошибка: не удалось декодировать файл (проверьте кодировку)")
    except OSError as e:
        print(f"Ошибка операционной системы: {e}")
    return None