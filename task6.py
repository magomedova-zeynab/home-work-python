from pathlib import Path
p = Path(path)
files = [f for f in p.iterdir() if f.is_file()]
dirs = [d for d in p.iterdir() if d.is_dir()]

py_files = [f for f in p.rglob("*.py") if f.is_file()]

total_size = sum(f.stat().st_size for f in p.rglob("*") if f.is_file())

print(f"Файлов в каталоге: {len(files)}")
print(f"Подкаталогов: {len(dirs)}")
print("Список .py файлов:")
for f in py_files:
    print(f"  {f}")
print(f"Суммарный размер всех файлов: {total_size} байт")