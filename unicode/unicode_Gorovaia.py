import unicodedata


def is_grapheme_cluster_boundary(prev_char, char):
    return unicodedata.combining(char) == 0


def generate_grapheme_clusters(text):
    text = unicodedata.normalize('NFD', text)
    clusters = []
    cluster_start = 0
    for i, char in enumerate(text):
        if i > 0 and is_grapheme_cluster_boundary(text[i - 1], char):
            clusters.append(text[cluster_start:i])
            cluster_start = i
    clusters.append(text[cluster_start:])
    normalized_clusters = [unicodedata.normalize('NFC', cluster) for cluster in clusters]
    return normalized_clusters


with open('sample.txt', 'r', encoding='utf-8') as file:
    text = file.read()

clusters = generate_grapheme_clusters(text)

output = ''
for i in clusters:
    if i == '\n':
        print(output[1:])
        output = ''
    else:
        output += "|" + i
