# Frequency Counter
def word_frequency(text: str) -> dict[str, int]:
    text = text.lower().strip()
    words: list = text.split()
    frequency: dict[str, int] = {}
    for word in words:
        frequency[word] = frequency.get(word,0)+1
    return frequency

text: str = "python is great and python is easy"
print(word_frequency(text))
text: str = str(input("enter a string"))
print(word_frequency(text))