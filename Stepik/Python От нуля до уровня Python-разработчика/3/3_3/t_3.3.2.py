def char_freq(text: str) -> dict[str, int]:
    char_dict = {}
    for char in text:
        if char not in char_dict:
            char_dict[char] = text.count(char)
    return char_dict

inp_text = input()
print(char_freq(inp_text))