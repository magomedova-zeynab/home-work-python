import re
from collections import Counter

def analyze_logs(path):
    level_counter = Counter()
    error_users = set()
    pattern = re.compile(r'\S+ \S+ (?P<level>INFO|WARNING|ERROR) User (?P<user>\d+)')

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            m = pattern.match(line)
            if not m:
                continue
            level = m.group('level')
            user = m.group('user')
            level_counter[level] += 1
            if level == 'ERROR':
                error_users.add(user)

    for level in ('INFO', 'WARNING', 'ERROR'):
        print(f"{level}: {level_counter.get(level, 0)}")

    if error_users:
        print("Пользователи с ошибками:", ", ".join(sorted(error_users)))


analyze_logs("app.log")