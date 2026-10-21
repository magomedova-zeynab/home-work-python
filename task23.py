import re

text = "Это   строка    с     большим    количеством   пробелов."
result = re.sub(r' {2,}', ' ', text)
print(result)

text2 = "   Текст   с   пробелами   "
result2 = re.sub(r' {2,}', ' ', text2).strip()
print(f"'{result2}'")