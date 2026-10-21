import re
import json
import logging
from collections import Counter

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def process_access_log(path):
    pattern = re.compile(
        r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+'
        r'(?P<method>GET|POST|PUT|DELETE|HEAD|OPTIONS)\s+'
        r'(?P<url>\S+)\s+'
        r'(?P<status>\d{3})'
    )

    method_counter = Counter()
    url_counter = Counter()
    errors_4xx = 0
    total = 0

    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                m = pattern.search(line)
                if not m:
                    logging.warning("Строка %d не соответствует формату: %s", line_num, line)
                    continue

                method = m.group('method')
                url = m.group('url')
                status = int(m.group('status'))

                method_counter[method] += 1
                url_counter[url] += 1
                total += 1
                if 400 <= status < 500:
                    errors_4xx += 1
    except FileNotFoundError:
        logging.error("Файл не найден: %s", path)
        return
    except PermissionError:
        logging.error("Нет прав на чтение файла: %s", path)
        return
    except OSError as e:
        logging.error("Ошибка ввода-вывода: %s", e)
        return

    most_common_url = url_counter.most_common(1)[0][0] if url_counter else None

    result = {
        "total_requests": total,
        "method_counts": dict(method_counter),
        "errors_4xx": errors_4xx,
        "most_common_url": most_common_url,
    }

    try:
        with open('stats.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        logging.info("Статистика сохранена в stats.json")
    except OSError as e:
        logging.error("Не удалось записать stats.json: %s", e)


process_access_log("access.log")