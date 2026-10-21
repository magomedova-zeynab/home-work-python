import re

def is_valid_login(login):
    return bool(re.fullmatch(r'[A-Za-z][A-Za-z0-9_]{3,15}', login))


tests = ["user_123", "admin", "123user", "ab", "user-name", "very_long_username"]
for t in tests:
    print(f"{t} -> {is_valid_login(t)}")