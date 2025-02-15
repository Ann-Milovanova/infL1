from collections import Counter
def find_repeated_pairs(text):
    pairs = [text[i:i + 2] for i in range(len(text) - 1)]
    return Counter(pairs)
def generate_codes(repeated_pairs):
    codes = {}
    unique_symbols = set()
    for pair in repeated_pairs:
        unique_symbols.add(pair)
    all_symbols = set(chr(i) for i in range(32, 127))
    available_symbols = list(all_symbols - unique_symbols)
    for i, pair in enumerate(repeated_pairs.keys()):
        if i < len(available_symbols):
            codes[pair] = available_symbols[i]
    return codes
def compress_text(text, codes):
    compressed_text = text
    for pair, code in codes.items():
        compressed_text = compressed_text.replace(pair, code)
    return compressed_text
def main():
    text = "пример текста для сжатия текста, текст содержит часто повторяющиеся пары букв."

    repeated_pairs = find_repeated_pairs(text)
    sorted_pairs = repeated_pairs.most_common()

    codes = generate_codes(dict(sorted_pairs))

    compressed_text = compress_text(text, codes)
    print("Таблица кодов:")
    for pair, code in codes.items():
        print(f"{pair} -> {code}")
    print("\nСжатый текст:")
    print(compressed_text)
if __name__ == "__main__":
    main()
