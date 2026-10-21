import re

def find_phones(text):
    pattern = re.compile(
        r'(?:\+7|8)\s*(?:\(\d{3}\)|\d{3})\s*\d{3}-\d{2}-\d{2}'
    )
    return pattern.findall(text)


sample = input()
for phone in find_phones(sample):
    print(phone)