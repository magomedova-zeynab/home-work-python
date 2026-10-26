from faker import Faker
import random

PUNCTUATION = ".,!?:;"


def generate_text_file(filename, sentences_count=10000):
    fake = Faker("ru_RU")

    with open(filename, "w", encoding="utf-8") as f:
        for _ in range(sentences_count):
            words = []
            for _ in range(random.randint(5, 18)):
                r = random.random()
                if r < 0.15:
                    words.append(fake.name())
                elif r < 0.30:
                    words.append(fake.city())
                else:
                    words.append(fake.word())

            sentence = " ".join(words).capitalize()
            f.write(sentence + random.choice([".", "!", "?"]) + "\n")


def count_words(filename):
    counts = {}

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            for ch in PUNCTUATION:
                line = line.replace(ch, " ")

            for word in line.lower().split():
                if word:
                    counts[word] = counts.get(word, 0) + 1

    top10 = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:10]
    return counts, top10


if __name__ == "__main__":
    filename = "text.txt"

    generate_text_file(filename, 10000)

    counts, top10 = count_words(filename)

    print(f"Всего уникальных слов: {len(counts)}")
    print("Топ-10 слов:")
    for word, freq in top10:
        print(f"  {word}: {freq}")