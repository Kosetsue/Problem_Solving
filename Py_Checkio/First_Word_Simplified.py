def first_word(text: str) -> str:
    lister = list(text.split())
    return lister[0]


print(first_word("Hello how are you"))
