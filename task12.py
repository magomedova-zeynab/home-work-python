import re

text = input()

emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
unique_emails = list(dict.fromkeys(emails))
for e in unique_emails:
    print(e)