def between_markers(text: str, start: str, end: str) -> str:
    start_index = text.index(start)
    end_index = text.index(end)
    found_text = text[start_index + 1 : end_index]

    return found_text


print("Example:")
print(between_markers("What is >apple<", ">", "<"))
