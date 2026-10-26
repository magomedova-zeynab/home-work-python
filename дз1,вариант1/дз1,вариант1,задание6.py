def analyze_journal(filename):
    total = count = count_ge_60 = 0
    max_score = min_score = None
    best_student = None

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")
            if len(parts) != 2:
                continue

            name, score_str = parts[0].strip(), parts[1].strip()
            try:
                score = int(score_str)
            except ValueError:
                continue

            if not name or not (0 <= score <= 100):
                continue

            total += score
            count += 1

            if max_score is None or score > max_score:
                max_score, best_student = score, name
            if min_score is None or score < min_score:
                min_score = score
            if score >= 60:
                count_ge_60 += 1

    if count == 0:
        return None

    return {
        "average": total / count,
        "max": max_score,
        "min": min_score,
        "count_ge_60": count_ge_60,
        "best_student": best_student,
    }


if __name__ == "__main__":
    result = analyze_journal("journal.txt")
    print(result if result else "Нет корректных данных")