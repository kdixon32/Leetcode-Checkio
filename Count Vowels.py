def count_vowels(text: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = text.lower()
    count = 0
    for i in range(0, len(text)):
        if text[i] in vowels:
            count+=1
    return count