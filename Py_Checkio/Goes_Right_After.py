def goes_after(word: str, first: str, second: str) -> bool:
    if first + second not in word:
        return False
    first_index = word.index(first)
    return first_index < word.index(second)


print("Example:")
print(goes_after("list", "l", "i"))
