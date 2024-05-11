import collections

def count_most_common_words(sample, n):
  
  with open(sample) as f:
    text = f.read()

  text = text.lower()

  words = text.split()

  counts = collections.Counter(words)

  most_frequent_words = counts.most_common(n)

  return most_frequent_words


sample = "sample.txt"
n = 100
most_frequent_words = count_words_from_file(sample, n)

print("Гистограмма:")
for word, count in most_frequent_words:
  print(f"{word:10} {count}")
