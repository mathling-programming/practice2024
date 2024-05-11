import unicodedata

def segment_text(text):

    segmented_text = []
    for char in text:
        segmented_text.append(char)
        if unicodedata.category(char) != "Mn":
            segmented_text.append("|")

    return "".join(segmented_text)


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        text = f.read()

    segmented_text = segment_text(text)

    print(segmented_text)
