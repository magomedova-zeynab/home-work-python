from pathlib import Path

def find_files(directory, extension):
    p = Path(directory)
    if not p.is_dir():
        print("Каталог не существует")
        return
    if not extension.startswith("."):
        extension = "." + extension
    found = False
    for f in p.rglob("*" + extension):
        if f.is_file():
            print(f"{f}  —  {f.stat().st_size} байт")
            found = True
    if not found:
        print("Файлы с указанным расширением не найдены")


find_files("project", ".py")   #пример