import re

with open("text11.txt", encoding="utf-8") as f:
    content = f.read()

all_ids = re.findall(r"User (\d+)", content)
error_lines = [line for line in content.splitlines() if "ERROR" in line]
error_ids = re.findall(r"ERROR User (\d+)", content)

print("Все ID:", all_ids)
print("Строки с ERROR:")
for line in error_lines:
    print(" ", line)
print("ID с ошибками:", error_ids)