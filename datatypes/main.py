from collections import Counter
import re


def plot_top_n_words_from_file(file_path, N):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    words = re.findall(r'\w+', text.lower())
    word_counts = Counter(words)
    top_n_words = word_counts.most_common(N)
    max_count = top_n_words[0][1]

    result_lines = []
    for word, count in top_n_words:
        bar = '#' * int((count / max_count) * 100)
        result_lines.append(f"{word:<20}|{bar} {count}")

    result_text = "\n".join(result_lines)
    print(result_text)


# Пример использования
file_path = 'sample.txt'  # Замените на путь к вашему файлу
plot_top_n_words_from_file(file_path, 100)
